#Bartosz Kosakowski
#reverses a string using recursion

def stringReverse(s):
    """
    takes a string s and reverses it using recursion
    """
    if len(s) == 1:
        return s[0]
    else:
        return s[len(s)-1] + stringReverse(s[:len(s)-1])
    
