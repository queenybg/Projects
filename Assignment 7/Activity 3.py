# This program calculates how much you have walked US Measurements or Metric Measurements. 
# The source code used for this program is python.


MILES_TO_YARDS = 1760
YARDS_TO_FEET = 3
FEET_TO_INCHES = 12

MILES_TO_KM = 1.609344
YARDS_TO_METERS = 0.9144
FEET_TO_CM = 30.48


def get_choice():
    print("Enter US to convert to US Measurements or M to convert to Metric Measurements:")
    choice = input()
    return choice


def get_miles(label):
    print(f"Enter {label} miles:")
    miles = float(input())
    return miles


def calculate_yards(miles):
    yards = miles * MILES_TO_YARDS
    return yards


def calculate_feet(yards):
    feet = yards * YARDS_TO_FEET
    return feet


def calculate_inches(feet):
    inches = feet * FEET_TO_INCHES
    return inches


def calculate_kilometers(miles):
    kilometers = miles * MILES_TO_KM
    return kilometers


def calculate_meters(yards):
    meters = yards * YARDS_TO_METERS
    return meters


def calculate_centimeters(feet):
    centimeters = feet * FEET_TO_CM
    return centimeters


def display_result(miles, from_label, result, to_label):
    print(f"{miles} miles, {from_label} yards,")
    print(f"{result} feet, and {to_label} inches.")


def display_result2(miles, from_label, result, to_label):
    print(f"{miles} miles, {from_label} kilometers,")
    print(f"{result} meters, and {to_label} centimeters.")


def main():
    choice = get_choice()
    if choice == "US" or choice == "us":
        miles = get_miles("miles")
        yards = calculate_yards(miles)
        feet = calculate_feet(yards)
        inches = calculate_inches(feet)
        display_result(miles, yards, feet, inches)
    elif choice == "M" or choice == "m":
        miles = get_miles("miles")
        kilometers = calculate_kilometers(miles)
        meters = calculate_meters(kilometers)
        centimeters = calculate_centimeters(meters)
        display_result2(miles, kilometers, meters, centimeters)
    else:
        print("You must enter US to convert to US measurements or M to convert to Metric measurements")

main()
