

def squareRootConvergents(N:int):
    count = 0
    n = 1
    d = 1
    ndigits = 10
    ddigits = 10
    for i in range(1, N+1):
        oldn = n
        n = (2 * d) + n
        d = d + oldn
        if n >= ndigits:
            ndigits *= 10
        if d >= ddigits:
            ddigits *= 10
        if ndigits > ddigits:
            count += 1
    return count


print(squareRootConvergents(1000))