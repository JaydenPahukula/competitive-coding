
A = 1504170715041707
B = 4503599627370517
invA = 3451657199285664

def p1(last:int):
    smallest = 10**22
    total = 0
    lastn = 0
    n = 0
    pattern = 1
    while 1:
        n += pattern
        m = (A*n) % B

        if m < smallest:
            total += m
            pattern = n-lastn
            print(n, m, total, "  ", smallest-m, "  ", pattern)
            lastn = n
            smallest = m
            if smallest == last:
                return total
        elif pattern != 1:
            pattern = 1
    return

def p2(last:int):
    total = 0
    m = 0
    d = {}
    for m in range(1, last):
        n = (m*invA) % B
        d[n] = m

    #print(d)
    smallest = last
    for n in sorted(d):
        if d[n] < smallest:
            total += d[n]
            print(n, d[n], total, "  ", smallest-d[n])
            smallest = d[n]

    return total

        

bp = 258162
print(p1(bp)+p2(bp))