for _ in range(int(input())):
    n,m = map(int, input().split())
    d = sorted(map(int, input().split()))
    t = 0
    score = 0
    i = 0
    while i < n and t+d[i]<=m:
        score += d[i]+1
        t += d[i]
        i += 1
    score += m-t
    print(score)