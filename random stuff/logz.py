import math

def logz(y2, y1):
    y2 = float(y2)
    y1 = float(y1)
    M = (math.log(y2, 2) - math.log(y1, 2))/(math.log(4096, 2) - math.log(1024, 2))
    print(y1/2**M)
    return M

def powerz(y2, y1):
    y2 = float(y2)
    y1 = float(y1)
    M = (math.log(y2, 2) - math.log(y1, 2))/(math.log(4096, 2) - math.log(1024, 2))
    A = (y1/2**M)
    return A*(2**14)**M
