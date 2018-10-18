from DownPayment import CertificateDeposit
from DownPayment import Calendar
import pytest
import math

def test_Construction():
    cd = CertificateDeposit.CertificateDeposit(start=Calendar.Calendar(10,2018), apy=1.2, term=3, principle=1)

    assert cd.getMatureDate().date() == (1,2019)

    cd2 = CertificateDeposit.CertificateDeposit(start=Calendar.Calendar(10,2018), apy=1.2, term=18, principle=1)
    assert cd2.getMatureDate().date() == (4,2020)

    # Check error conditions on construction
    with pytest.raises(AssertionError):
        cd1 = CertificateDeposit.CertificateDeposit(start=None, apy=1.2, term=3)
        cd2 = CertificateDeposit.CertificateDeposit(start=Calendar.Calendar(2,2000), apy=-1, term=3, principle=1)
        cd3 = CertificateDeposit.CertificateDeposit(start=Calendar.Calendar(2,2000), apy=101, term=3, principle=1)
        cd4 = CertificateDeposit.CertificateDeposit(start=Calendar.Calendar(2,2000), apy=1, term=-3, principle=1)
        cd5 = CertificateDeposit.CertificateDeposit(start=Calendar.Calendar(2,2000), apy=1, term=3, principle=-1)


def test_valueCalculation():
    cd = CertificateDeposit.CertificateDeposit(start=Calendar.Calendar(10,2018), apy=1.2, term=4, principle=14)

    expectedValue = 14.056084056
    assert math.fabs(cd.getMaturityValue() - expectedValue) < 1.0e-10