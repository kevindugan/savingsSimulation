from DownPayment import SavingsAccount, Calendar, CertificateDeposit
import pytest
import math

def test_Construction():

    acc = SavingsAccount.SavingsAccount()
    assert acc.getStartDate() is None
    assert acc.getEndDate() is None
    assert acc.getMonthlyContribution() == []

def test_SetAndGet():

    acc = SavingsAccount.SavingsAccount()

    acc.setStartDate((6,2018))
    date = Calendar.Calendar(6,2018)
    assert acc.getStartDate().isDateSame(date.date())

    acc.setEndDate((7,2018))
    date.setDate(7,2018)
    assert acc.getEndDate().isDateSame(date.date())

    with pytest.raises(AssertionError):
        acc.setStartDate((8,2018))
    with pytest.raises(AssertionError):
        acc.setEndDate((5,2018))

def test_BalanceWithContribution():

    acc = SavingsAccount.SavingsAccount()

    acc.setStartDate((6,2018))
    acc.setEndDate((3,2019))
    acc.addMonthlyContribution(12.0)

    balance = acc.calculateBalance()

    expectedBalance = [12.0, 24.0, 36.0, 48.0, 60.0, 72.0, 84.0, 96.0, 108.0, 120.0]

    for result, expected in zip(balance, expectedBalance):
        assert result == expected

def test_BalanceWithCD():

    acc = SavingsAccount.SavingsAccount()

    acc.setStartDate((6,2018))
    acc.setEndDate((3,2019))
    
    cd1 = CertificateDeposit.CertificateDeposit(Calendar.Calendar(6,2018), 1.2, 4, 14.0)
    acc.addCertificateDeposit(cd1)

    balance = acc.calculateBalance()

    expectedBalance = [14, 14.014, 14.028014, 14.042042014, 14.056084056, 14.056084056, 14.056084056, 14.056084056, 14.056084056, 14.056084056]

    assert len(balance) == len(expectedBalance)
    for result, expected in zip(balance, expectedBalance):
        assert math.fabs(expected - result ) < 5.0e-11, "Diff = " + str(math.fabs(expected - result ))

def test_BalanceWithCDandContribution():

    acc = SavingsAccount.SavingsAccount()

    acc.setStartDate((6,2018))
    acc.setEndDate((3,2019))

    acc.addMonthlyContribution(10.0)

    cd1 = CertificateDeposit.CertificateDeposit(Calendar.Calendar(8,2018), 1.2, 4, 14.0)
    acc.addCertificateDeposit(cd1)

    balance = acc.calculateBalance()

    expectedBalance = [10, 20, 44, 54.014, 64.028014, 74.042042014, 84.056084056, 94.056084056, 104.056084056, 114.056084056]

    assert len(balance) == len(expectedBalance)
    for result, expected in zip(balance, expectedBalance):
        assert math.fabs(expected - result ) < 5.0e-11, "Diff = " + str(math.fabs(expected - result ))