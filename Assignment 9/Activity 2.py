def playGame(guesses, guessNumber, lowpoint, highpoint):
    while True:    #This simulates a Do Loop
        print("My guess is " + str(guessNumber) + " was my guess too high (h), too low (l), or equal(e) to your number?")
        response = input()
        if response == "h" or response == "high":
            highpoint = guessNumber
            guesses = guesses + 1
            guessNumber = float(highpoint - lowpoint) / 2 + lowpoint
            if guessNumber <= lowpoint:
                guessNumber = guessNumber + 1
            if highpoint - lowpoint == 2:
                guessNumber = lowpoint + 1
        else:
            if response == "l" or response == "low":
                lowpoint = guessNumber
                guesses = guesses + 1
                guessNumber = float(highpoint - lowpoint) / 2 + lowpoint
                if guessNumber <= lowpoint:
                    guessNumber = guessNumber + 1
                if highpoint - lowpoint == 2:
                    guessNumber = lowpoint + 1
            else:
                if response == "e" or response == "equal":
                    result(guessNumber, guesses)
        if not(guesses >= 0): break   #Exit loop

def result(guessNumber, guesses):
    print("I guessed your number! And it only took me " + str(guesses) + " guesses!")

# Main
# This is a program that can guess your number. I am using python as my source code for the program.
guesses = 1
guessNumber = 50
lowpoint = 1
highpoint = 100
playGame(guesses, guessNumber, lowpoint, highpoint)

