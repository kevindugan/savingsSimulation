from DownPayment import Calendar
import pytest

def test_Construction():
    month = Calendar.Calendar(month=1, year=2018)
    assert month.date() == (1, 2018)

    # Check that assertion on month range gets activated
    with pytest.raises(AssertionError):
        month = Calendar.Calendar(month=0)
    with pytest.raises(AssertionError):
        month = Calendar.Calendar(month=13)

def test_AddMonths():
    start = Calendar.Calendar(month=6, year=2018)

    expectedDates = [(6,2018), 
                     (7,2018), (8,2018), (9,2018), (10,2018), (11,2018), (12,2018),
                     (1,2019), (2,2019), (3,2019), (4,2019), (5,2019), (6,2019),
                     (7,2019), (8,2019), (9,2019), (10,2019), (11,2019), (12,2019),
                     (1,2020), (2,2020), (3,2020), (4,2020), (5,2020), (6,2020),
                     (7,2020), (8,2020), (9,2020), (10,2020), (11,2020), (12,2020),
                     (1,2021)]
    for index, date in zip( range(len(expectedDates)), expectedDates):
        assert start.getFutureDate(index) == date

    # Check that passing negative months errors
    with pytest.raises(AssertionError):
        start.getFutureDate(-1)

def test_CreateFutureDate():

    start = Calendar.Calendar(month=6, year=2018)

    date1 = start.makeFutureDate(0)
    assert date1.date() == (6,2018)
    date2 = start.makeFutureDate(1)
    assert date2.date() == (7,2018)
    date3 = start.makeFutureDate(7)
    assert date3.date() == (1,2019)

    # Check that passing negative months errors
    with pytest.raises(AssertionError):
        start.makeFutureDate(-1)


def test_Comparison():

    start = Calendar.Calendar(month=6, year=2018)

    assert start.isDateBefore((5,2018))
    assert start.isDateBefore((6,2017))
    assert start.isDateBefore((8,2017))
    assert not start.isDateBefore((6,2018))
    assert not start.isDateBefore((7,2018))
    assert not start.isDateBefore((5,2019))

    assert start.isDateSame((6,2018))
    assert not start.isDateSame((7,2018))
    assert not start.isDateSame((5,2018))
    assert not start.isDateSame((6,2017))
    assert not start.isDateSame((6,2019))

    assert not start.isDateAfter((5,2018))
    assert not start.isDateAfter((6,2017))
    assert not start.isDateAfter((8,2017))
    assert not start.isDateAfter((6,2018))
    assert start.isDateAfter((7,2018))
    assert start.isDateAfter((5,2019))

    # Check that passing invalid date format throws error
    with pytest.raises(AssertionError):
        start.isDateBefore((1,2,3))
    with pytest.raises(AssertionError):
        start.isDateBefore((13,2))
    with pytest.raises(AssertionError):
        start.isDateBefore((-1,3))


def test_GetTerm():

    start = Calendar.Calendar(month=6, year=2018)

    testDates = [(6,2018),
                 (7,2018), (8,2018), (9,2018), (10,2018), (11,2018), (12,2018),
                 (1,2019), (2,2019), (3,2019), (4,2019), (5,2019), (6,2019),
                 (7,2019), (8,2019), (9,2019), (10,2019), (11,2019), (12,2019),
                 (1,2020), (2,2020), (3,2020), (4,2020), (5,2020), (6,2020),
                 (7,2020), (8,2020), (9,2020), (10,2020), (11,2020), (12,2020),
                 (1,2021)]
    for index, date in zip( range(len(testDates)), testDates):
        assert start.getTerm(date) == index

    assert start.getTerm((4,2283)) == 3178

    with pytest.raises(AssertionError):
        start.getTerm((5,2018))

def test_getTermAxisLabel():

    start = Calendar.Calendar(month=6, year=2018)

    finalDate = (10, 2021)
    expectedLabels = [""]*(start.getTerm(finalDate)+1)
    expectedLabels[0] = "Jun-2018"
    expectedLabels[-1] = "Oct-2021"
    expectedLabels[7:-1:12] = ["Jan-2019", "Jan-2020", "Jan-2021"]
    resultLabel = start.getTermAxisLabel(finalDate)

    for expected, result in zip (expectedLabels, resultLabel):
        assert expected == result

def test_dateWords():

    start = Calendar.Calendar(month=6, year=2018)

    testDates = [(6,2018),
                 (7,2018), (8,2018), (9,2018), (10,2018), (11,2018), (12,2018),
                 (1,2019), (2,2019), (3,2019), (4,2019), (5,2019), (6,2019),
                 (7,2019), (8,2019), (9,2019), (10,2019), (11,2019), (12,2019),
                 (1,2020), (2,2020), (3,2020), (4,2020), (5,2020), (6,2020),
                 (7,2020), (8,2020), (9,2020), (10,2020), (11,2020), (12,2020),
                 (1,2021)]

    expectedDates = ["June 2018",
                     "July 2018", "August 2018", "September 2018", "October 2018", "November 2018", "December 2018",
                     "January 2019", "February 2019", "March 2019", "April 2019", "May 2019", "June 2019",
                     "July 2019", "August 2019", "September 2019", "October 2019", "November 2019", "December 2019",
                     "January 2020", "February 2020", "March 2020", "April 2020", "May 2020", "June 2020",
                     "July 2020", "August 2020", "September 2020", "October 2020", "November 2020", "December 2020",
                     "January 2021"]

    for date, expected in zip(testDates, expectedDates):
        assert start.convertDateToWords(date) == expected