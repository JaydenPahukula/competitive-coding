import math

n, p, s, v = map(float, input().split())

def time(c:float):
    return (s * (1 + 1/c) / v) + (n * (math.log(n, 2)**(c * (math.sqrt(2)))) / (p * (10**9)))

def ternarySearch(start=0.0, end=100.0):
    mid1 = start + (end-start)/3
    mid2 = end - (end-start)/3
    tmid1 = time(mid1)
    tmid2 = time(mid2)
    if abs(mid1-mid2) < 0.00000001:
        print(tmid1, mid1)
    elif tmid1 > tmid2:
        ternarySearch(mid1, end)
    else:
        ternarySearch(start, mid2)
    return

ternarySearch()