
class Calendar(object):

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

    def makeFutureDate(self, nMonths):
        assert nMonths >= 0

        date = self.getFutureDate(nMonths)
        return Calendar(month=date[0], year=date[1])

    def isDateBefore(self, date=None):
        assert type(date) is tuple and len(date) is 2
        assert date[0] > 0 and date[0] <= 12

        if date[1] < self.year:
            return True
        elif date[1] == self.year:
            if date[0] < self.month:
                return True
            elif date[0] == self.month:
                return False
            elif date[0] > self.month:
                return False
            else:
                raise RuntimeError("Date Comparison Failed, Month="+str(date[0]))
        elif date[1] > self.year:
            return False
        else:
            raise RuntimeError("Date Comparison Failed, Year="+str(date[1]))

    def isDateSame(self, date=None):
        assert type(date) is tuple and len(date) is 2
        assert date[0] > 0 and date[0] <= 12

        if date[0] == self.month and date[1] == self.year:
            return True
        else:
            return False

    def isDateAfter(self, date=None):
        if not self.isDateSame(date) and not self.isDateBefore(date):
            return True
        else:
            return False