# This program uses a python source code to calculate your high, low, and average score.
# Then sort the entered grades from lowest to highest.


def get_scores():
    test_scores = []
    value = 0
    while value >= 0:
        value = float(input('Enter score: '))
        if value > 0:
            test_scores.append(value)
        else:
            return test_scores


def get_total(value_list):
    total = float(0)
    for num in value_list:
        total += float(num)
    return total


def main():
    scores = get_scores()
    total = get_total(scores)
    average = total/len(scores)
    print('The lowest score is: ', min(scores))
    print('The highest score is: ', max(scores))
    print('The average is: ', average)
    print('Sorted grades', sorted(scores))
    print('Total is: ', total)


main()
