def one_mode(l):
    n=0
    i=0
    while i < len(l):
        if l.count(l[i])>n:
            n=l.count(l[i])
            o=i
            i=i+1
        else:
            i=i+1
    return ((l[o]),n)

def all_modes(l):
    n=0
    i=0
    o=0
    p=set()
    while i < len(l):
        if l.count(l[i])>=n:
            n=l.count(l[i])
            i=i+1
        else:
            i=i+1
    while o < len(l):
        if l.count(l[o])==n:
            p.add(l[o])
            o=o+1
        else: o=o+1
    return (p,n)
