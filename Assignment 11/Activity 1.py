# This program uses python source code to tell you what year is a leap year.
# Along with how many days are in each month.


months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def get_year():
    year = int(input("Enter year: "))
    return year


def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("is a leap year")
        days[2] = 29
    else:
        print("is not a leap year")


def get_month():
    month = int(input("Enter a month: "))
    return month


def get_months(month):
    while month < 13 and month > 0:
        print(months[month], "has", days[month], "days")
        month = int(input("\nEnter a month: "))
    if month > 13:
        print('Invalid input. Please enter months between 1-12')


def main():
    year = get_year()
    leap_year(year)
    month = get_month()
    get_months(month)


main()
