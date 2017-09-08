#Bartosz Kosakowski
#400028494
#Lab 4 Question 2
####################

def median(l):
    if len(l)%2 != 0:
        midIndex = (len(l))//2
        median = l[midIndex]
    else:
        median = ((l[len(l)//2]) + (l[len(l)//2-1]))/2
    return median
        
