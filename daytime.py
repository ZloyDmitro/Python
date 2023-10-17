from datetime import datetime, timedelta, date
import calendar
current_datetime = datetime.now()
print(current_datetime.year)

#Task2
some_date = datetime(2021, 7, 14)
print(some_date.weekday())

print(calendar.month(2021,2))
leap_year = calendar.isleap(2021)
print(leap_year)

#Task 3
year = input("Please input a year to check:\n")
def ifleapyear(year):
    year = int(year)
    if calendar.isleap(year):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is NOT leap year")

ifleapyear(year)

#Task 4

from datetime import datetime

#date_as_string = "Feb 14 2021 8:30AM"
date_as_string = input("Please input date to check:\n")
input_format = "%b %d %Y %I:%M%p"
date_as_datetime = datetime.strptime(date_as_string, input_format)
result = date_as_datetime.strftime("%Y-%m-%d %H:%M:%S")

print(result)
