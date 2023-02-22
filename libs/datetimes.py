import datetime


def is_weekday(today):
    day_number = today.weekday()

    return day_number < 5  # 5 Sat, 6 Sun


def is_weekend(today):
    day_number = today.weekday()

    return day_number >= 5  # 5 Sat, 6 Sun

