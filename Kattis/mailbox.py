n = int(input())
for _ in range(n):
    k,m = map(int, input().split())
    lo = 0
    for _ in range(k-1):
        lo = (lo+m)//2
    print(m*(m+1)//2 - lo*(lo+1)//2)
