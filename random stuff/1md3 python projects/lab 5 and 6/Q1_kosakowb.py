#Bartosz Kosakowski
#400028494
#Lab 5/6 Question 1
####################

class ChangeRemainderError(Exception):
    pass

class ChangeParameterError(Exception):
    pass

def change(a, d):
    """ Computes the change of amount a given denominations d. Parameter
    a must be of type int, d must be of type list of int, and the
    elements of d must be in ascending order, otherwise
    ChangeParameterError is raised. The result is a list of the same
    length as d consisting of pairs with the number of coins / bills of
    each denomination. This is computed by first taking the maximal
    number of coins / bill of the highest denomination, then the next
    highest, etc. If no exact change is possible, ChangeRemainderError
    is raised."""
    ...
    if type(a) == int and type(d) == list:
        checkList = sorted(d)
        changeList = d
        changeRemainder = a
        changeReturn = []
        changeCheck = 0
        if d != checkList:
            raise ChangeParameterError
        else:
            for i in range(len(changeList),0,-1):
                changeMult = changeRemainder//changeList[i-1]
                changeRemainder = changeRemainder - (changeList[i-1]*changeMult)
                changeReturn.append(changeMult)
                changeCheck = changeCheck + changeList[i-1]*changeMult
            changeReturn.reverse()
            if changeCheck != a:
                raise ChangeRemainderError
        return changeReturn         
    else:
        raise ChangeParameterError
        
