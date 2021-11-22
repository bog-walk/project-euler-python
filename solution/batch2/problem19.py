""" Problem 19: Counting Sundays

https://projecteuler.net/problem=19

Goal: Find the number of Sundays that fell on the 1st day of the month between
2 dates YYYY MM DD inclusive.

Constraints: 1900 <= Y1 <= 10^16, Y1 <= Y2 <= Y1 + 1000,
             1 <= M1, M2 <= 12,
             1 <= D1, D2 <= 31

e.g.: Y1 M1 D1 = 1900 1 1, Y2 M2 D2 = 1910 1 1
      num of Sundays on the 1st = 18
"""


def get_weekday(day, month, year):
    """
    Zeller's Congruence algorithm returns the weekday for any date based on the formula:
    h = (day + (13*(month+1)/5) + K + (K/4) + (J/4) + 5*J) % 7;
    with month & year being adjusted to have January and February as the 13th & 14th months
    of the preceding year, and (K, J) = (year % 100, year / 100).
    Note that this only applies to the Gregorian calendar.
    @:return    integer from 0 to 6 with 0 = Saturday, 1 = Sunday, ..., 6 = Friday.
    """
    if month < 3:
        month += 12
        year -= 1
    k, j = year % 100, year // 100
    return (day + 13 * (month + 1) // 5 + k + k // 4 + j // 4 + 5 * j) % 7


def count_sundays_zellers(start_y, start_m, start_d, end_y, end_m):
    # Adjust starting month forward as only the weekday on the first of the month matters
    if start_d > 1:
        start_m = start_m % 12 + 1
        # Adjust starting year forward if date has rolled over
        # e.g. Dec 2, 2020 would become Jan 1, 2021
        if start_m == 1:
            start_y += 1
    sundays = 0
    # End loop when end month & year exceeded, as end day is not relevant
    while start_y <= end_y:
        if start_y == end_y and start_m > end_m:
            break
        # Use Zeller's congruence to check if first of month is Sunday
        if get_weekday(1, start_m, start_y) == 1:
            sundays += 1
        # Move forward to next month
        start_m = start_m % 12 + 1
        if start_m == 1:
            start_y += 1
    return sundays


days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year):
    return year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0)


def get_january_first(year):
    """
    Iterative search returns weekday on January 1st of provided year,
    based on the fact that Jan 1st, 1900 was a Monday. Sunday = 0.
    """
    start = 1900
    day = 1
    while start < year:
        day = (day + 2) % 7 if is_leap_year(start) else (day + 1) % 7
        start += 1
    return day


def count_sundays_firsts(start_y, start_m, start_d, end_y, end_m, end_d):
    """
    Consider using memoisation to improve performance when evaluating dates
    in the upper constraints.
    """
    # Adjust starting month & year
    if start_d > 1:
        start_m = start_m % 12 + 1
        if start_m == 1:
            start_y += 1
    sundays = 0
    # Get weekday that corresponds to Jan 1st of starting year
    jan_first = get_january_first(start_y)
    # Use above weekday to find first Sunday in January that year
    day = 1 if jan_first == 0 else 8 - jan_first
    if start_y == end_y and start_m > end_m:
        return sundays
    if day == 1:
        sundays += 1
    while start_y <= end_y:
        # Jump forward a week as only interested in checking every Sunday
        day += 7
        if start_m == 2 and is_leap_year(start_y):
            month_days = 29
        else:
            month_days = days_in_month[start_m - 1]
        if day > month_days:
            day -= month_days
            start_m += 1
        if start_y == end_y and start_m == end_m and day > end_d:
            break
        if day == 1:
            sundays += 1
        if start_m > 12:
            start_y += 1
            start_m = 1
    return sundays
