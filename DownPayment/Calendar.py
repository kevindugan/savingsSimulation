
class Calendar():

    def __init__(self, month=None, year=None):
        assert month > 0 and month <= 12
        self.month = month
        self.year = year

    def date(self):
        return (self.month, self.year)

    def getFutureDate(self, nMonths):
        assert nMonths >= 0
        futureMonth = self.month + nMonths - 1

        newMonth = (futureMonth % 12) + 1
        newYear  = int(futureMonth / 12) + self.year

        return (newMonth, newYear)

