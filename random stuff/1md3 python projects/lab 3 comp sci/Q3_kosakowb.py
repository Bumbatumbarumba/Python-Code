#Bartosz Kosakowski
#400028494
#Lab 3 Question 2
####################

def roman(n: 'an integer between 1 and 999'):
    romanNumsTuple = (('CM',900),('D',500),('CD',400),('C',100),('XC',90),('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',4),('I',1))  
    romanNums = ''
    if n < 1 or n > 999:
        print('Please enter a number between 1 and 999')
    else:
        for romanTuple in romanNumsTuple:
            while n-romanTuple[1] >=0:
                n = n-romanTuple[1]
                romanNums = romanNums + romanTuple[0]
    return romanNums
