#Bartosz Kosakowski
#400028494
#Lab 5/6 Question 4
####################
from random import *

def craps():
    initialRoll = randint(1,12)
    if initialRoll == 2 or initialRoll == 3 or initialRoll == 12:
        print(initialRoll)
        return 0
    elif initialRoll == 7 or initialRoll == 11:
        print(initialRoll)
        return 1
    else:
        nextRoll = randint(1,6) + randint(1,6)
        
def manyCraps(n):
    totalRolls = n
    winCount = 0
    while n > 0:
        initialRoll = randint(1,6) + randint(1,6)
        if initialRoll == 2 or initialRoll == 3 or initialRoll == 12:
            winCount = winCount
        elif initialRoll == 7 or initialRoll == 11:
            winCount = winCount + 1   
        else:
            nextRoll = randint(1,6) + randint(1,6)
            j = 1
            while j > 0:
                if nextRoll == initialRoll:
                    winCount = winCount + 1
                    j = 0
                elif nextRoll == 7:
                    winCount = winCount
                    j = 0
                else:
                    nextRoll = randint(1,6) + randint(1,6)
                    j = j
        n = n-1
    return (winCount/totalRolls)
