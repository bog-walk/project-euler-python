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
from datetime import timedelta, datetime


def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0)


def get_january_first(year: int) -> int:
    """
    Brute search finds weekday on January 1st of provided year,
    based on the fact that Jan 1st, 1900 was a Monday. Sunday = 0.

    :returns: Integer from 0 to 6 with 0 = Sunday.
    """

    start = 1900
    day = 1
    while start < year:
        day = (day + 2) % 7 if is_leap_year(start) else (day + 1) % 7
        start += 1
    return day


def count_sundays_firsts(
        start_y: int, start_m: int, start_d: int,
        end_y: int, end_m: int, end_d: int
) -> int:
    """
    This solution will not tolerate years > 1e6 well.

    SPEED (WORSE): 0.6555s for 1000 year delta in the upper constraints.
    """

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # adjust starting month & year
    if start_d > 1:
        start_m = start_m % 12 + 1
        if start_m == 1:
            start_y += 1
    sundays = 0
    # get weekday that corresponds to Jan 1st of starting year
    jan_first = get_january_first(start_y)
    # use above weekday to find first Sunday in January that year
    day = 1 if jan_first == 0 else 8 - jan_first
    if start_y == end_y and start_m > end_m:
        return sundays
    if day == 1:
        sundays += 1
    while start_y <= end_y:
        # jump forward a week as only interested in checking every Sunday
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


def get_weekday(day: int, month: int, year: int) -> int:
    """ Find the weekday for a date using Zeller's Congruence algorithm.

    Zeller's Congruence algorithm is based on the formula:

    h = (day + (13 * (month + 1) / 5) + K + (K / 4) + (J / 4) + 5 * J) % 7,
    with month & year being adjusted to have January and February as the 13th &
    14th months of the preceding year, and (K, J) = (year % 100, year / 100).
    Note that this only applies to the Gregorian calendar.

    :returns: Integer from 0 to 6 with 0 = Saturday, 1 = Sunday, ..., 6 = Friday.
    """

    if month < 3:
        month += 12
        year -= 1
    k, j = year % 100, year // 100
    return (day + 13 * (month + 1) // 5 + k + k // 4 + j // 4 + 5 * j) % 7


def count_sundays_zellers(
        start_y: int, start_m: int, start_d: int, end_y: int, end_m: int
) -> int:
    """
    SPEED (BEST): 0.0158s for 1000 year delta in the upper constraints.
    """

    # adjust starting month forward
    # as only the weekday on the first of the month matters
    if start_d > 1:
        start_m = start_m % 12 + 1
        # adjust starting year forward if date has rolled over
        # e.g. Dec 2, 2020 would become January 1st, 2021
        if start_m == 1:
            start_y += 1
    sundays = 0
    # end loop when end month & year exceeded, as end day is not relevant
    while start_y <= end_y:
        if start_y == end_y and start_m > end_m:
            break
        # check if first of month is Sunday
        if get_weekday(1, start_m, start_y) == 1:
            sundays += 1
        # move forward to next month
        start_m = start_m % 12 + 1
        if start_m == 1:
            start_y += 1
    return sundays


def count_sundays_firsts_library(
        start_y: int, start_m: int, start_d: int,
        end_y: int, end_m: int, end_d: int
) -> int:
    """
    Uses the datetime library to facilitate quick movement through the given dates,
    as well as built-in determination of the associated weekday and comparison of
    the dates to end the search.

    For the dates to work with the library functions, the years must first be
    normalised using the pattern that the calendar cycles every 400 years, unless
    that period crosses over into a new century (it cycles every 28 years if that
    century is a leap year).

    SPEED (BETTER): 0.0197s for 1000 year delta in the upper constraints.
    """

    year_norm = (start_y % 400) + 400
    end_y = end_y - start_y + year_norm
    start = datetime(year_norm, start_m, start_d)
    end = datetime(end_y, end_m, end_d)
    count = 0
    step = timedelta(days=1)
    while start <= end:
        # find first day of month that is a Sunday, if any
        if start.day == 1 and start.weekday() == 6:
            count += 1
            # check only every Sunday after that
            step = timedelta(days=7)
        start += step
    return count
