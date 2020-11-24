# This program shows how much you make in a week, month and a year.

MONTHS_PER_YEAR = 12
WEEKS_PER_YEAR = 52


def get_hours():
    print("Enter how many hours do you work a week:")
    hours = float(input())
    return hours


def get_rate():
    print("Enter rate per hour:")
    rate = float(input())
    return rate


def calculate_weekly(hours, rate):
    weekly_pay = (hours * rate)
    return weekly_pay


def calculate_monthly(weekly_pay):
    monthly_pay = (weekly_pay * WEEKS_PER_YEAR / MONTHS_PER_YEAR)
    return monthly_pay


def calculate_yearly(monthly_pay):
    yearly_pay = (monthly_pay * WEEKS_PER_YEAR)
    return yearly_pay


def display_result(weekly_pay, monthly_pay, yearly_pay):
    print ("You get paid: " + str(weekly_pay) + " a week,")
    print (monthly_pay, " a month, and " + str(yearly_pay) + " a year.")


def main():
    hours = get_hours()
    rate = get_rate()
    weekly_pay = calculate_weekly(hours, rate)
    monthly_pay = calculate_monthly(weekly_pay)
    yearly_pay = calculate_yearly(monthly_pay)
    display_result(weekly_pay, monthly_pay, yearly_pay)

main()
