#This program is using the python source code to calculate your average grade score.


def get_score():
    score = float(input("Enter grade scores (negative number to end): "))
    return score


def get_average():
    score = 0       
    count = 0       
    total = 0       
    while score >= 0:       
        score = get_score()
        if score >= 0:         
            total = total + score               
            count = count + 1               
    if count > 0:
        average = total / count
    else:
        average = 0

    return average


def display_average(average):
    print("Your average is", average)


def main():
    average = get_average()
    display_average(average)


main()
