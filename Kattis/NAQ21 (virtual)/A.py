n = int(input())
l = [int(c) for c in str(n)]
s = set(l)
if len(s) == 10:
    print("impossible")
elif s == {1,2,3,4,5,6,7,8,9}:
    print(0)
else:
    hi = []
    lo = []
    for i in range(len(l)):
        if i == 0 or hi[i-1] == l[i-1]: digithi = l[i]
        else: digithi = 0
        while sum([1 for c in str(digithi) if int(c) in s])>0: digithi += 1
        hi.append(digithi)
        if i == 0 or lo[i-1] == l[i-1]: digitlo = l[i]
        else: digitlo = 9
        while digitlo in s and digitlo != 0: digitlo -= 1
        lo.append(digitlo)
    hi = int("".join(map(str, hi)))
    lo = int("".join(map(str, lo)))
    if hi-n == n-lo: print(lo, hi)
    elif hi-n < n-lo: print(hi)
    else: print(lo)