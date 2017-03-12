#Bartosz Kosakowski
#testing readlines function

def sortTextDoc(src,dst):
    s = open(src,'r')
    d = open(dst,'w')
    testList = list(s.readlines())
    print(testList)
    
    if testList[len(testList)-1][len(testList[len(testList)-1])-1] != '\n':
        testList[len(testList)-1] = str(testList[len(testList)-1]) + '\n'

    testList = sorted(testList)
    print(testList)
    
    for i in range(len(testList)):
        d.write(str(testList[i]))
    
    s.close()
    d.close()
    
    
