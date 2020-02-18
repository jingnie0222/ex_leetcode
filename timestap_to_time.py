#!/usr/bin/python3
# -*-codig=utf8-*-
month_day = {1: 31,
             2: 28,
             3: 31,
             4: 30,
             5: 31,
             6: 30,
             7: 31,
             8: 31,
             9: 30,
             10: 31,
             11: 30,
             12: 31}

def leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True

    return False

def timestap_to_datetime(timestap):

    second = timestap % 60
    miniute = int(timestap/60) % 60
    hour = int(timestap/3600) % 24 + 8
    print("Result: %02d:%02d:%02d" % (hour, miniute, second))

    year = 1970
    days = (timestap/(3600*24)) + 1

    while True:
        if leap_year(year):
            day_remain = days - 366
        else:
            day_remain = days - 365

        if day_remain > 0:
            year += 1
            days = day_remain
        else:
            break

    month = 1
    while True:
        if leap_year(year) and month == 2:
            day_remain = days - month_day[month] - 1
        else:
            day_remain = days - month_day[month]

        if day_remain > 0:
            month += 1
            days = day_remain
        else:
            break

    print("%d-%02d-%02d" % (year, month, days))






timestap_to_datetime(1561781019)