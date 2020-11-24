def calculateDays(years):
    days = years * 365
    
    return days

def calculateHours(days):
    hours = days * 24
    
    return hours

def calculateMonths(years):
    months = years * 12
    
    return months

def calculateSeconds(hours):
    seconds = hours * 60 * 60
    
    return seconds

def getYears():
    print("how old are you?")
    years = float(input())
    
    return years

def result(years, months, days, hours, seconds):
    print("You are: " + str(years) + " years old, and " + str(months) + " months old, " + str(days) + " days old, " + str(hours) + " hours old, and " + str(seconds) + " seconds old.")

# Main
# This program calculates your age and it displays how long you've lived for in months,days,hours and seconds. I use Python as my source code to describe how long a person has lived for.
years = getYears()
months = calculateMonths(years)
days = calculateDays(years)
hours = calculateHours(days)
seconds = calculateSeconds(hours)
result(years, months, days, hours, seconds)
