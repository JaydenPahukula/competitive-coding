for _ in range(int(input())):
    n, W = map(int, input().split())
    a = list(map(int, input().split()))
    lo = min(a)
    hi = max(a)+100000000000
    while lo < hi-1:
        mid = (hi+lo)//2
        w = sum([max(mid-a[i],0) for i in range(n)])
        if w > W: hi = mid
        else: lo = mid
    print(lo)      