import sys
input=sys.stdin.readline

MOD = 10**9+7

out = []
for _ in range(int(input())):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    best = 0
    i = 0
    while i < n:
        runningSum = 0
        while i < n:
            if a[i] < 0: best = max(best, runningSum)
            if -a[i] < runningSum: runningSum += a[i]
            else:
                runningSum = 0
                break
            i += 1
        best = max(best, runningSum)
        i += 1
    
    total = 0
    for i in range(n): total = (total+a[i])%MOD
    thing = ( (best%MOD) * (((2<<k-1)-1)%MOD) )%MOD
    total = (total+thing)%MOD

    out.append(total)
print("\n".join(map(str, out)))
