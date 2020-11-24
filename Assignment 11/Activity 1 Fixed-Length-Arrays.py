# This program uses python source code to calculate your, high, low, and average scores.


def number_tests():
    print("How many test scores do you want? ")
    nbr_tests = int(input())
    return nbr_tests


def test_score(number_of_test):
    array_of_scores = [0] * number_of_test
    for x in range(number_of_test):
        print("Enter your scores: ")
        array_of_scores[x] = float(input())
    return array_of_scores


def tests_stats(array_of_scores, number_of_tests):
    sum = 0
    highest = array_of_scores[0]
    lowest = array_of_scores[0]
    for x in range(number_of_tests):
        if(array_of_scores[x] < lowest):
            lowest = array_of_scores[x]
        if(array_of_scores[x] > highest):
            highest = array_of_scores[x]
        sum = sum + array_of_scores[x]
    average = float(sum)/number_of_tests
    return average, highest, lowest


def result(average, highest, lowest):
    print("The average of the scores is: ", average)
    print("The highest score is: ", highest)
    print("The lowest score is: ", lowest)


def main():
    number_of_tests = number_tests()
    score_array = test_score(number_of_tests)
    average, highest, lowest = tests_stats(score_array, number_of_tests)
    result(average, highest, lowest)


main()
