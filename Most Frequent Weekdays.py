import datetime


def most_frequent_days(year):
    years = datetime.datetime(year, 12, 31)
    days = int(years.strftime('%j'))
    sort = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    common = [datetime.datetime(year, 12, 31).strftime('%A')] if days == 365 else sorted([datetime.datetime(year, 12, 30).strftime('%A'), datetime.datetime(year, 12, 31).strftime('%A')], key = sort.index)
    return common
