def orderTotals(src, dst):
    s = open(src,'r')
    d = open(dst,'w')
    orders = {}
    for line in s:
        fields = line.split()
        #precondition: fields[0] is not empty
        if len(fields) >= 2:
            try:
                numOrdered = int(fields[1])
            except:
                numOrdered = 1
        else:
            numOrdered = 1
        if fields[0] != '':
            #precondition: field[0] is not empty
            if fields[0] in orders:
                orders[fields[0]] = numOrdered + orders[fields[0]]
            else:
                order[fields[0]] = numOrdered
    for item in orders:
        if orders[item] > 1:
            plural = 's'
        else:
            plural = ''
        d.write(str(orders[item]) + " " + item + plural + 'ordered')
    s.close()
    d.close()
