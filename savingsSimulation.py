from DownPayment import SavingsAccount
from DownPayment import CertificateDeposit, Calendar

def main():
    account = SavingsAccount.SavingsAccount()
    account.setStartDate((10,2018))
    account.setEndDate((12,2021))
    account.setGoal(40000.0)
    account.setStartingBalance(4609.29)

    account.addMonthlyContribution(1600.0)
    cds = []
    cds += [CertificateDeposit.CertificateDeposit(Calendar.Calendar(month=10,year=2018), 2.7, 17, 4609.29)]
    account.addCertificateDeposit(cds[-1])

    cds += [CertificateDeposit.CertificateDeposit(Calendar.Calendar(month=1, year=2019), 1.65, 17, 4800.0)]
    account.addCertificateDeposit(cds[-1])


    cds += [CertificateDeposit.CertificateDeposit(Calendar.Calendar(month=4, year=2019), 1.4, 14, 4800.0)]
    account.addCertificateDeposit(cds[-1])

    cds += [CertificateDeposit.CertificateDeposit(Calendar.Calendar(month=7, year=2019), 1.4, 12, 4800.0)]
    account.addCertificateDeposit(cds[-1])

    account.addDeposit(Calendar.Calendar(month=11,year=2019), 3800.0)

    # account.plotSimulation()
    account.printBalance()
    for cd in cds:
        print("Interest Earned: {0:7.2f}, Matured: {1:s}".format( cd.getMaturityValue()-cd.principle, Calendar.Calendar.convertDateToWords(cd.getMatureDate().date()) ))

if __name__ == "__main__":
    main()