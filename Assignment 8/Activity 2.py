# This program calculates your average grade score.


def number_of_scores():
    print("How many scores do you want to enter?")
    number = float(input())
    return number


def while_loop(number):
    count = 0
    total = 0
    while count < number:
        count = count + 1
        score = float(input("Enter a score: "))
        total = total + score
        if count == number:
            break
    totals = total
    average = totals / number
    print("Your total average is: ", average)


def main():
    number = number_of_scores()
    while_loop(number)


main()
