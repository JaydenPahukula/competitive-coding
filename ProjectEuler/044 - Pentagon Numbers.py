import math

def isPentagonal(num:int):
    x = (math.sqrt(1 + 24 * num) + 1) / 6
    if x % 1 == 0:
        return True
    return False


def findPentagonalPairs(n:int):
    dmin = 100000000000
    for n1 in range(1, n):
        p1 = n1 * (3 * n1 - 1) / 2
        for n2 in range(n1 + 1, n):
            p2 = n2 * (3 * n2 - 1) / 2
            if isPentagonal(p1 + p2) and isPentagonal(p2 - p1):
                d = abs(p2 - p1)
                if d < dmin:
                    print(p1, p2)
                    dmin = d
    return dmin

print(findPentagonalPairs(10000))