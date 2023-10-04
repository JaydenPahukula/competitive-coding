a, b, n = map(float, input().split())

PI = 3.14159265359
def sliceArea(lo, hi):
    return a**2*hi**3/24/PI + a*b*hi**2/4 + PI*b**2*hi/2 - a**2*lo**3/24/PI - a*b*lo**2/4 - PI*b**2*lo/2

eachSlice = sliceArea(0, 2*PI) / n
start = 0
for i in range(int(n)-1):
    hi = 2*PI
    lo = start
    while abs(hi-lo) > 0.00000001:
        mid = (hi+lo)/2
        if sliceArea(start, mid) > eachSlice: hi = mid
        else: lo = mid
    start = lo
    print(lo)