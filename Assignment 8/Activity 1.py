def getExpressions():
    print("How many expressions do you want?")
    expressions = float(input())
    
    return expressions

def getValue():
    print("Enter a value:")
    value = float(input())
    
    return value

def whileLoop(value, expressions):
    print("While loop is listing multiplication expressions for the value of " + str(value) + " :")
    count = 1
    while count <= expressions:
        print(str(value) + " * " + str(count) + " = " + str(count * value))
        count = count + 1

# Main
# This is a multiplication program that asks the user to input a value that they want to multiply by, and then how many expressions the user wants.
value = getValue()
expressions = getExpressions()
whileLoop(value, expressions)
