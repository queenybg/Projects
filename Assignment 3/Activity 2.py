# This program calculates your age and it displays how long you've liced for in months,days,hours and seconds. I use Python as my source code to describe how long a person has lived for.
print("How old are you?")
years = float(input())
months = years * 12
days = years * 365
hours = days * 24
seconds = hours * 60 * 60
print("You are: " + str(years) + " years old, " + str(months) + " months old, " + str(days) + " days old, " + str(hours) + " hours old, and " + str(seconds) + " seconds old.")
