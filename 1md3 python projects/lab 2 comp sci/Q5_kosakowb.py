#Bartosz Kosakowski
#400028494
#Lab 2 Question 5
###################
def exp(x: 'an integer',y: 'a non-negative integer'):
    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        i = 0
        calcExp = 1
        while i < y:
            calcExp = calcExp*x
            i = i+1
        return calcExp
