n, lo, hi = map(int, input().split())
l = sorted([int(input()) for _ in range(n-1)])
needhi = l[-1] != hi
needlo = l[0] != lo
if needhi and needlo:
    print(-1)
elif needhi:
    print(hi)
elif needlo:
    print(lo)
else:
    print("\n".join([str(x) for x in range(lo, hi+1)]))