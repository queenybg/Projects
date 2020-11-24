# This program calculates how much you have walked in yards,feet and inches.

MILES_TO_YARDS = 1760
YARDS_TO_FEET = 3
FEET_TO_INCHES = 12

miles = input("How many miles did you walk today?")
miles = float(miles)

yards_walked = miles * MILES_TO_YARDS
feet_walked = yards_walked * YARDS_TO_FEET
inches_walked = feet_walked * FEET_TO_INCHES

print("You have walked:", yards_walked, "yards")
print(feet_walked, "feet")
print(inches_walked, "inches")