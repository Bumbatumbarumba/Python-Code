def removePunct(aString):
    newString = ""
    for letter in aString:
        if letter == "," or letter == "." or letter == ";" or letter == "!" or letter == "?":
            letter = ""
        newString += letter
    print(newString)

    
    
def removePunct2(aString):
    newString = ""
    puncts = [",", "!", "?", ".", "(", ")"]
    for letter in aString:
        if letter in puncts:
            letter = ""
        newString += letter
    print(newString)
