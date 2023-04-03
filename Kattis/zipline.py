import math

for _ in range(int(input())):
    w, g, h, r = map(int, input().split())
    g -= r
    h -= r

    def cablelength(x:float):
        return math.sqrt((g**2) + (x**2)) + math.sqrt((h**2) + (w-x)**2)

    def ternarySearch(start:float=0, end:float=w):
        mid1 = start + (end-start)/3
        mid2 = end - (end-start)/3
        mid1len = cablelength(mid1)
        mid2len = cablelength(mid2)
        if abs(mid1-mid2) < 0.0000000001:
            return mid1len
        elif mid1len < mid2len:
            return ternarySearch(start, mid2)
        else:
            return ternarySearch(mid1, end)

    tautlen = math.sqrt((w**2) + (abs(g-h)**2))
    print(tautlen, ternarySearch())