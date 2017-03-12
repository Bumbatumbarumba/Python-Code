#Bartosz Kosakowski
#400028494
#Lab 4 Question 1
##################

def one_mode(l: 'list of numbers'):
    numList = sorted(l,reverse = True)
    modeCount = []
    for i in range(len(numList)):
        x = numList[i]
        y = numList.count(numList[i])
        if numList[i] == numList[i-1]:
            numList = numList[:i]
        else:
            z = (x,y)
            modeCount.append(z)
    print(modeCount)
