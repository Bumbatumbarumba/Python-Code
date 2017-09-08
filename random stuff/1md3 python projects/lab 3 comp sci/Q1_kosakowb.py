#Bartosz Kosakowski
#400028494
#Lab 3 Question 1
####################

def shorten(s: 'a string'):
    newStr = ''
    for i in s:
        if 'a' <= i <= 'z':
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                i = ''
        elif 'A' <= i <= 'Z':
            if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
                i = ''
        newStr = newStr + i
    return s

def shortenPlus(s: 'a string'):
    i = 0
    while i < len(s):
        if ('a' <= s[i] <= 'z') and (s[i-1] != ' ') and (i != 0):
            if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
                 s = s[:i] + s[i+1:]
                 i = i-1

        elif ('A' <= s[i] <= 'Z') and (s[i-1] != ' ') and (i != 0):
            if s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U':
                 s = s[:i] + s[i+1:]
                 i = i-1
        i = i+1
    return s
