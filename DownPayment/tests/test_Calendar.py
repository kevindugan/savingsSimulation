from DownPayment import Calendar
import pytest

def test_Construction():
    month = Calendar.Calendar(month=1, year=2018)
    assert month.date() == (1, 2018)

    # Check that assertion on month range gets activated
    with pytest.raises(AssertionError):
        month = Calendar.Calendar(month=0)
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

    with pytest.raises(AssertionError):
        start.getFutureDate(-1)