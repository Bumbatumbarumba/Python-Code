#Bartosz Kosakowski
#400028494
#Lab 3 Question 4
####################

def factorial(B):
    if B == 0:
        return 1
    else:
        return B*factorial(B-1)

def cfac(n, k):
    num1 = factorial(n)
    num2 = factorial(k)
    num3 = factorial(n-k)
    biCoeff = int(num1/(num2*num3))
    return biCoeff
