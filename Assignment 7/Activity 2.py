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

def displayResult(years, result, label):
    print("You are: " + str(years) + " years old, and " + str(result) + " " + label + " old.")

def getChoice():
    print("How would you like your age to be displayed? M or m for months, D or d for days, H or h for hours, or S and s for seconds:")
    choice = input()
    
    return choice

def getYears():
    print("Enter your age:")
    years = float(input())
    
    return years

def processDays():
    years = getYears()
    result = calculateDays(years)
    displayResult(years, result, "days")

def processHours():
    years = getYears()
    days = calculateDays(years)
    result = calculateHours(days)
    displayResult(years, result, "hours")

def processMonths():
    years = getYears()
    result = calculateMonths(years)
    displayResult(years, result, "months")

def processSeconds():
    years = getYears()
    days = calculateDays(years)
    hours = calculateHours(days)
    result = calculateSeconds(hours)
    displayResult(years, result, "seconds")

# Main
# This program calculates how old you are in months, days, hours or seconds. So which ever one you choose it will display it. I am using python as the source code to describe the program.
choice = getChoice()
if choice == "M" or choice == "m":
    processMonths()
else:
    if choice == "D" or choice == "d":
        processDays()
    else:
        if choice == "H" or choice == "h":
            processHours()
        else:
            if choice == "S" or choice == "s":
                processSeconds()
            else:
                print("You must enter Months, Days, Hours or Seconds in order to calculate your age.")
