#TEXT PARSER
#Created by Bartosz Kosakowski
#January 5th, 2017 @12:51am

def textParser(test):
    textToParse = test.split(" ")
    movementVerbs = ["go", "move", "walk", "step", "relocate", "turn", "translate", "strafe", "crawl", "tip-toe", "slither", "hobble", "limp", "strut", "stumble", "run", "sprint", "bolt", "journey", "retreat", "travel"]
    directions = ["up", "down", "left", "right", "forward", "forwards", "backward", "backward"]
    gettingThings = ["grab", "take", "pick up"]
    for word in textToParse:
        if word in movementVerbs:
            print (words + " is a movement verb")
        elif word in :
            print (words + " is not a movement verb")
