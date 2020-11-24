# This program shows how much you make in a week, month and a year.

MONTHS_PER_YEAR = 12
WEEKS_PER_YEAR = 52

hours = input("Enter how many hours you work a week: ")
hours = float(hours)

rate = input("Enter Rate per Hour: ")
rate = float(rate)

pay = hours * rate
income_per_month = pay * WEEKS_PER_YEAR / MONTHS_PER_YEAR
income_per_year = pay * WEEKS_PER_YEAR

print("You get paid:", pay, "a week")
print(income_per_month, "a month")
print(income_per_year, "a year")