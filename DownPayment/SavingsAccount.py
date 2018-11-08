from DownPayment import Calendar, CertificateDeposit
import matplotlib.pyplot as plt
import numpy
from prettytable import PrettyTable

class SavingsAccount(object):

    def __init__(self):
        self.monthlyContribution = []
        self.certificateDeposits = []
        self.deposits = []
        self.startDate = None
        self.endDate = None
        self.goal = 0.0
        self.startingBalance = 0.0

    def setStartingBalance(self, balance=None):
        assert balance >= 0.0
        self.startingBalance = balance

    def setGoal(self, amount=None):
        assert amount >= 0.0
        self.goal = amount

    def setStartDate(self, start=None):
        assert type(start) is tuple and len(start) is 2
        assert start[0] > 0 and start[0] <= 12
    
        newDate = Calendar.Calendar(start[0], start[1])
        if self.endDate is not None:
            assert self.endDate.isDateBefore(newDate.date())

        self.startDate = newDate

    def addDeposit(self, date=None, amount=None):
        assert type(date) == Calendar.Calendar
        assert date.isDateBefore(self.startDate.date()) and date.isDateAfter(self.endDate.date())
        assert amount >= 0.0

        self.deposits += [(date, amount)]

    def getStartDate(self):
        return self.startDate

    def setEndDate(self, end=None):
        assert type(end) is tuple and len(end) is 2
        assert end[0] > 0 and end[0] <= 12

        newDate = Calendar.Calendar(end[0], end[1])
        if self.startDate is not None:
            assert self.startDate.isDateAfter(newDate.date())

        self.endDate = newDate

    def getEndDate(self):
        return self.endDate

    def addMonthlyContribution(self, amount=None):
        assert amount >= 0.0

        self.monthlyContribution += [amount]

    def addCertificateDeposit(self, cd=None):
        assert type(cd) == CertificateDeposit.CertificateDeposit
        assert cd.getStartDate().isDateBefore(self.startDate.date()) or cd.getStartDate().isDateSame(self.startDate.date())

        self.certificateDeposits += [cd]

    def getMonthlyContribution(self):
        return self.monthlyContribution

    def getTermLength(self):
        return self.startDate.getTerm(self.endDate.date())

    def calculateGoal(self):
        termLength = self.getTermLength()
        return [self.goal] * (termLength+1)

    def calculateBalance(self):
        termLength = self.getTermLength()
        available = numpy.zeros(termLength+1) + self.startingBalance
        unavailable = numpy.zeros(termLength+1)

        # print("Balance")
        # print("Available: "+str(["%5.2f" % member for member in available]))

        monthlyCont = 0.0
        for deposit in self.monthlyContribution:
            monthlyCont += deposit

        for index in range(termLength+1):
            available[index] = available[index-1] + monthlyCont

        for deposit in self.deposits:
            dateOffset = self.startDate.getTerm(deposit[0].date())
            available[dateOffset:] += deposit[1]

        # print("Available: "+str(["%5.2f" % member for member in available]))
        for cd in self.certificateDeposits:
            startDate = cd.getStartDate()
            startOffset = self.startDate.getTerm(startDate.date())
            # Move Funds from Available to Unavailable
            available[startOffset:] -= cd.principle
            unavailable[startOffset:(startOffset+cd.term+1)] += cd.getMonthlyValue()
            unavailable[(startOffset+cd.term+1):] += cd.getMaturityValue()

            # Move Funds back to available after maturity
            unavailable[(startOffset+cd.term+1):] -= cd.getMaturityValue()
            available[(startOffset+cd.term+1):] += cd.getMaturityValue()
        # print("Available: "+str(["%5.2f" % member for member in available]))

        return (available, unavailable, available+unavailable)

    def plotSimulation(self):
        plt.figure()

        xlabel = self.startDate.getTermAxisLabel(self.endDate.date())
        termLength = self.getTermLength()

        plt.xticks(range(termLength+1), xlabel, rotation=70)
        plt.ylim([0, self.goal*2])

        plt.step(range(termLength+1), self.calculateGoal())
        plt.step(range(termLength+1), self.calculateBalance()[-1])

        plt.show()

    def printBalance(self):
        monthLabel = []
        for month in range(self.getTermLength()):
            monthLabel += [self.startDate.convertDateToWords(self.startDate.getFutureDate(month))]

        available, unavailable, balance = self.calculateBalance()
        formattedAvailable = [ SavingsAccount.formatNumber(member) for member in available]
        formattedUnavailable = [ SavingsAccount.formatNumber(member) for member in unavailable]
        formattedBalance = [ SavingsAccount.formatNumber(member) for member in balance]

        table = PrettyTable()

        table.field_names = ["Month", "Available Funds", "Unavailable Funds", "Total Balance"]
        table.align = "r"

        printedLimit = [False, False]
        maxLength = [max(monthLabel, key=len), max(formattedAvailable, key=len), max(formattedUnavailable, key=len), max(formattedBalance, key=len)]
        maxLength = [ len(max(index, index2)) for index, index2 in zip(table.field_names, maxLength)]
        for month, avail, unavail, bal in zip(monthLabel, formattedAvailable, formattedUnavailable, formattedBalance):
            table.add_row([month,avail,unavail,bal])
            if float(SavingsAccount.unformatNumber(bal)) >= self.goal and not printedLimit[0]:
                table.add_row(['-'*maxLength[0], '-'*maxLength[1], '-'*maxLength[2], '-'*maxLength[3]])
                printedLimit[0] = True
            if float(SavingsAccount.unformatNumber(avail)) >= self.goal and not printedLimit[1]:
                table.add_row(['='*maxLength[0], '='*maxLength[1], '='*maxLength[2], '='*maxLength[3]])
                printedLimit[1] = True

        print(table)

    @staticmethod
    def formatNumber(number):
        value = number
        thousands = int(value/1000)
        leftover = value - thousands * 1000
        valueFormat = "{0:06.2f}".format(leftover)
        if thousands > 0:
            valueFormat = "{0:3d},".format(thousands) + valueFormat

        return valueFormat.strip()

    @staticmethod
    def unformatNumber(number):
        return "".join(number.split(','))
