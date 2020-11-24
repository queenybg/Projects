# This is a multiplication program that asks the user to input a value that they want to multiply by.


def get_value(label):
    print("Enter " + label + " value:")
    value = int(input())
    return value


def table(start, end):
    print('', end='\t')
    for i in range(start, end + 1):
        print(i, end='\t')
    print('')

    for i in range(start, end + 1):
        print(i, end='\t')
        for j in range(start, end + 1):
            print(i * j, end='\t')
        print('')


def main():
    start = get_value("starting")
    end = get_value("ending")
    table(start, end)


main()
