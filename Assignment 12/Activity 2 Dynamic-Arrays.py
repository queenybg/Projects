# This is a program is using python source code to guess your number.


def game():
   low = 0
   high = 100
   guesses = []
   while True:
       guess = (high + low)//2
       print('Is your secret number ' + str(guess) + '?')
       answer = input("Enter high(h), low(l), or equal(e) when I guess correctly:")
       if answer == 'h' or answer == 'high':
        low = guess
        guesses.append(answer)
       elif answer == 'l' or answer == 'low':
        high = guess
        guesses.append(answer)
       elif answer == 'e' or answer == 'equal':
        print("Game over. It took me", len(guesses),"guesses.")
        break
       else:
        print('Sorry, I did not understand your input.')


def main():
    game()


main()
