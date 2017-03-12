#Derivative calculator
#created by Bartosz Kosakowski
#16/01/17
import re
def findPolyDerivative(myExpr):
    splitExpr = re.split("([+-/*^])", myExpr.replace(" ", ""))
    result = []
    for i in range(len(splitExpr)):
        if splitExpr[i] == "^":
            splitExpr[i+1] = str(int(splitExpr[i+1]) - 1)
    return splitExpr
