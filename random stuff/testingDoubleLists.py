def dListA():
    test = []
    jList = []
    temp = []
    for i in range(12):
        for j in range(8):
            temp = jList.append(i)
        test.append(jList)
        jList = []
    print(test)

def dListB(a, b):
    test = []
    for y in range(b):
        test.append([y for x in range(a)])
    print(test)
