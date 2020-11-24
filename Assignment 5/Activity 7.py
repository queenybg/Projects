def dogname():
    print("what is the name of your dog?")
    dogname = input()
    
    return dogname

def calculateDogyears(humanyears):
    dogyears = humanyears * 7
    
    return dogyears

def calculateHumanyears():
    print("How old is your dog in human years?")
    humanyears = float(input())
    
    return humanyears

def result(dogname, dogyears):
    print("Your dog " + dogname + " is " + str(dogyears) + " dog years old. ")

# Main
# This program coverts human year to dog years. It shows how old a dog is from human years to dog years. Used python as my source code language to show how old a dog is coverted from human years to dog years.
dogname = dogname()
humanyears = calculateHumanyears()
dogyears = calculateDogyears(humanyears)
result(dogname, dogyears)
