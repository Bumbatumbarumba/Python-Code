#Bartosz Kosakowski
#testing read function

def readTest(src):
    s = open(src,'r')
    test = s.read()
    s.close()
    return test
