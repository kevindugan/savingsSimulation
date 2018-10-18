from DownPayment import Calendar

class CertificateDeposit(object):

    def __init__(self, start=None, apy=None, term=None, principle=None):
        assert type(start) is Calendar.Calendar
        assert apy > 0.0 and apy <= 100.0
        assert term >= 0
        assert principle >= 0.0
        
        self.startDate = start
        self.percentageYield = apy
        self.term = term
        self.principle = principle
        self.matureDate = self.startDate.makeFutureDate(term)

    def getMatureDate(self):
        return self.matureDate

    def getMaturityValue(self):
        factor = (1.0 + (self.percentageYield/100.0/12.0))**self.term

        return self.principle * factor