#Bartosz Kosakowski
#400028494
#Lab 2 Question 4
#####################

#takes a string and makes it plural
def pluralPlus(x):
    if x.endswith('s'):
        x = x + 'es'
    elif x.endswith('h'):
        x = x + 'es'
    elif x.endswith('y'):
        x = x[:(len(x)-1)] + 'ies'
    else:
        x = x + 's'
    return x
