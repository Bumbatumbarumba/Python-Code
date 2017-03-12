#Bartosz Kosakowski
#400028494
#Lab 5 Bonus Question 1
########################

def averageLineLength(fn):
    s = open(fn, 'r')
    lineList = list(s)
    charSum = 0
    for i in range(len(lineList)):
        charSum = charSum + len(lineList[i])
    charSum = charSum - (len(lineList)-1)
    print(charSum)
    print(lineList)
    print(len(lineList))
    return charSum/len(lineList)
    s.close()
