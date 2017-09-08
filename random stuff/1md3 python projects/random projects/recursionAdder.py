#Bartosz Kosakowski
#recursion practise

def recursionAdder(n):
    """takes a number n and adds its components, eg n = 3 -> 3+2+1
    """
    total = 0
    if n == 0:
        return 0
    else:
        return n + recursionAdder(n-1)
