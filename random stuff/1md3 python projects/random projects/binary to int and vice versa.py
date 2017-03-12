def intToBinary(n):
    s = str(n%2)
    while n>1:
        n = n//2
        s = str(n%2)+s
    return s

def binaryToInt(b):
    n = 0
    for c in b:
        n = 2*n+int(c)
    return n
