#Bartosz Kosakowski
#400028494
#Lab 3 Question 8
####################

def similarity(s, t):
    simCount = 0
    wordLong = s
    wordShort = t
    
    if len(wordShort) > len(wordLong):
        wordLong = t
        wordShort = s
        
    for i in wordShort:
        for j in wordLong:
            if i == j:
                simCount = simCount + 1
                if simCount > len(wordShort):
                    simCount = len(wordShort)
                
    return simCount
