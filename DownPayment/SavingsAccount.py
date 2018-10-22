from DownPayment import Calendar, CertificateDeposit
import matplotlib.pyplot as plt
import numpy

class SavingsAccount(object):

    def __init__(self):
        self.monthlyContribution = []
        self.certificateDeposits = []
        self.startDate = None
        self.endDate = None
        self.goal = 0.0

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
        balance = numpy.zeros(termLength+1)
        # print(["%5.2f" % member for member in balance])

        monthlyCont = 0.0
        for deposit in self.monthlyContribution:
            monthlyCont += deposit

        for index in range(termLength+1):
            balance[index] += balance[index-1] + monthlyCont

        # print(["%5.2f" % member for member in balance])
        for cd in self.certificateDeposits:
            startDate = cd.getStartDate()
            startOffset = self.startDate.getTerm(startDate.date())
            startingBalance = balance[startOffset:(startOffset+cd.term+1)]
            balance[startOffset:(startOffset+cd.term+1)] = cd.getMonthlyValue() + startingBalance

            maturityValue = cd.getMaturityValue()
            balance[(startOffset+cd.term+1):] += maturityValue
        # print(["%5.2f" % member for member in balance])

        return balance

    def plotSimulation(self):
        plt.figure()

        xlabel = self.startDate.getTermAxisLabel(self.endDate.date())
        termLength = self.getTermLength()

        plt.xticks(range(termLength+1), xlabel, rotation=70)
        plt.ylim([0, self.goal*2])

        plt.step(range(termLength+1), self.calculateGoal())
        plt.step(range(termLength+1), self.calculateBalance())

        plt.show()

    def printBalance(self):
        monthLabel = []
        for month in range(self.getTermLength()):
            monthLabel += [self.startDate.convertDateToWords(self.startDate.getFutureDate(month))]

        balance = self.calculateBalance()
        formattedBalance = ["%12.2f" % member for member in balance]

        maxLength = len(max(monthLabel, key=len))
        printedLimit = False
        for month, amount in zip(monthLabel, formattedBalance):
            pad = ' '* (maxLength - len(month))
            print(pad+month+": "+amount)
            if float(amount) >= self.goal and not printedLimit:
                print('-'*(maxLength+2+12)+" Goal = "+str(self.goal))
                printedLimit = True