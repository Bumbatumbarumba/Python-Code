#Bartosz Kosakowski
#400028494
#Lab 5 Question 5
#################

class FileNotFoundError(Exception):
    pass

def sortbytime(src,dst):
    try:
        s = open(src,'r')
        d = open(dst, 'w')
        lineList = list(s.readlines())
        if lineList[len(lineList)-1][len(lineList[len(lineList)-1])-1] != '\n':
            lineList[len(lineList)-1] = str(lineList[len(lineList)-1]) + '\n'
        lineList = sorted(lineList)
        for i in range(len(lineList)):
            d.write(str(lineList[i]))   
        s.close()
        d.close()
    except:
        raise FileNotFoundError
        
    
    
