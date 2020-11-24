def forLoop(value, expressions):
    print("Listing multiplication expressions for the value of " + str(value) + " :")
    count = 1
    for count in range(1, expressions + 1, 1):
        print(str(value) + " * " + str(count) + " = " + str(count * value))

def getExpressions():
    print("How many expressions do you want?")
    expressions = int(input())
    
    return expressions

def getValue():
    print("Enter a value:")
    value = int(input())
    
    return value

# Main
# This is a multiplication program that asks the user to input a value that they want to multiply by, and then how many expressions the user wants.
value = getValue()
expressions = getExpressions()
forLoop(value, expressions)
