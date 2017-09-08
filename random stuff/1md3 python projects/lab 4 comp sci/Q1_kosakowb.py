#Bartosz Kosakowski
#400028494
#Lab 4 Question 1
##################

def one_mode(l: 'list of numbers'):
    numCount,i = 0,0
    while i< len(l):
        if l.count(l[i]) > numCount:
            numCount = l.count(l[i])
            j = i
            i = i+1
        else:
            i = i+1
    return((l[j]),numCount)


def all_modes(l: 'list of numbers'):
    numCount,i,j = 0,0,0
    modeSet = set()
    while i < len(l):
        if numCount <= l.count(l[i]):
            numCount = l.count(l[i])
        else:
            pass
        i = i+1
    while j < len(l):
        if numCount == l.count(l[j]):
            modeSet.add(l[j])
        else:
            pass
        j = j+1
    return (modeSet,numCount)
