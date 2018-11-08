from DownPayment import SavingsAccount
from DownPayment import CertificateDeposit, Calendar

def main():
    account = SavingsAccount.SavingsAccount()
    account.setStartDate((10,2018))
    account.setEndDate((12,2021))
    account.setGoal(40000.0)
    account.setStartingBalance(4609.29)

    # Setting up simulation
    account.addMonthlyContribution(1600.0)
    cds = []

    # Bought this cd apy=2.7, term=17 on Oct 18
    cds += [CertificateDeposit.CertificateDeposit(Calendar.Calendar(month=10,year=2018), 2.7, 17, 4609.29)]
    account.addCertificateDeposit(cds[-1])


    # Below is plan to buy
    cds += [CertificateDeposit.CertificateDeposit(Calendar.Calendar(month=1, year=2019), 1.65, 18, 6400.0)]
    account.addCertificateDeposit(cds[-1])
    cds += [CertificateDeposit.CertificateDeposit(Calendar.Calendar(month=4, year=2019), 1.4, 15, 4800.0)]
    account.addCertificateDeposit(cds[-1])
    cds += [CertificateDeposit.CertificateDeposit(Calendar.Calendar(month=7, year=2019), 1.4, 12, 4800.0)]
    account.addCertificateDeposit(cds[-1])
    cds += [CertificateDeposit.CertificateDeposit(Calendar.Calendar(month=11, year=2019), 0.2, 8, 10200)]
    account.addCertificateDeposit(cds[-1])

    # Planned Deposit from TDECU
    account.addDeposit(Calendar.Calendar(month=11,year=2019), 3800.0)

    # account.plotSimulation()
    account.printBalance()
    for cd in cds:
        value = cd.getMaturityValue()-cd.principle
        thousands = int(value/1000)
        leftover = value - thousands * 1000
        valueFormat = "{0:6.2f}".format(leftover)
        if thousands > 0:
            valueFormat = " {0:3d},".format(thousands) + valueFormat
        else:
            valueFormat = "     " + valueFormat
        print("Interest Earned: {0:s}, Matured: {1:s}".format( valueFormat, Calendar.Calendar.convertDateToWords(cd.getMatureDate().date()) ))

if __name__ == "__main__":
    main()
