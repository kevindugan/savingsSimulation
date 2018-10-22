from DownPayment import SavingsAccount
from DownPayment import CertificateDeposit, Calendar

def main():
    account = SavingsAccount.SavingsAccount()
    account.setStartDate((6,2018))
    account.setEndDate((12,2020))
    account.setGoal(40000.0)

    account.addMonthlyContribution(1600.0)
    # cd1 = CertificateDeposit.CertificateDeposit(Calendar.Calendar(month=6,year=2018), 2.7, 17, 4609.29)
    # account.addCertificateDeposit(cd1)

    account.plotSimulation()
    account.printBalance()

if __name__ == "__main__":
    main()