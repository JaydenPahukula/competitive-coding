for _ in range(int(input())):
    n, h = map(int, input().split())
    l = list(map(int, input().split()))
    maxPossible = [l[i+1]-l[i] for i in range(n-1)]
    def damage(k): return k+sum([min(k, maxPossible[i]) for i in range(n-1)])
    lo = 0
    hi = 10**18
    while hi-lo != 1:
        m = (lo+hi)//2
        if damage(m)>=h: hi=m
        else: lo=m
    print(hi)
