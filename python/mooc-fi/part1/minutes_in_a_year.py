# Program: minutes_in_a_year.py
# Author:  Nuhu Hamidu
# Purpose: A program to print out the number of minutes in a year.

# Assuming an ordinary year (non-leap year).
# minutes_per_year = days_per_year * hours_per_day * minutes_per_hour
DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60

minutes_per_year = DAYS_PER_YEAR * HOURS_PER_DAY * MINUTES_PER_HOUR
print("Minutes in a year:")
print(minutes_per_year)
