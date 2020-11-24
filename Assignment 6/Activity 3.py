# This program calculates how much you have walked in yards,feet and inches.

MILES_TO_YARDS = 1760
YARDS_TO_FEET = 3
FEET_TO_INCHES = 12


def get_miles():
    print("How many miles did you walk today?")
    miles = float(input())
    return miles


def yards_walked(miles):
    yards = miles * MILES_TO_YARDS
    return yards


def feet_walked(yards):
    feet = yards * YARDS_TO_FEET
    return feet


def inches_walked(feet):
    inches = feet * FEET_TO_INCHES
    return inches


def display_result(miles, yards, feet, inches):
    print("You have walked: " + str(yards) + " yards, ")
    print(feet, "feet and, " + str(inches) + " inches. ")


def main():
    miles = get_miles()
    yards = yards_walked(miles)
    feet = feet_walked(yards)
    inches = inches_walked(feet)
    display_result(miles, yards, feet, inches)

main()
