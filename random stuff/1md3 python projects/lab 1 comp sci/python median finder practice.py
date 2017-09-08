x=3
y=2
z=1
if x<y:
    if z<x:
        m=x
        print("The median is ",m)
    elif z<y:
        m=z
        print("The median is ",m)
    else:
        m=y
        print("The median is ",m)
else:
    if x<z:
        m=x
        print("The median is ",m)
    elif z<y:
        m=y
        print("The median is ",m)
    else:
        m=z
        print("The median is ",m)
