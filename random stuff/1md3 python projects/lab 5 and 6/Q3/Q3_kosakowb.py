#Bartosz Kosakowski
#400028494
#Lab 5/6 Question 3
#####################

def sortFile(src,dst):
    s = open(src, 'r')
    d = open(dst, 'w')
    lineList = list(s)
    lineList.sort()
    for i in range(len(lineList)):
        if lineList[i] == '\n':
            lineList[i] = ""
        d.write(str(lineList[i]))
    s.close()
    d.close()
