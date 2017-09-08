#Bartosz Kosakowski
#400028494
#Lab 2 Question 8
###################
def onlyLetters(s):
    s = s.lower()
    i = 0
    while i < len(s) - 1:
        #note: I was told to only account for commas, periods, exclamation marks,
        #question marks and apostrophes (with regards to punctuation)
        if s[i] == ' ' or s[i] == '.' or s[i] == ',' or s[i] == '!' or s[i] == '?' or s[i] == '\'':
            s = s[:i] + s[i+1:]
        i = i+1
    return s

def isPalindromePlus(s):
    q = onlyLetters(s)
    for i in range(len(q)//2):
        if q[i] != q[-i-1]: return False
    return True

def palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]: return False
    return True
