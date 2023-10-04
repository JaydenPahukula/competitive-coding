INFINITY = 12395873149875901278345.12459871457098
while 1:
    n = int(input())
    if n == 0: break
    points = [tuple(map(int, input().split())) for _ in range(n)]
    best = 1
    for i in range(n-1):
        x1,y1 = points[i]
        counts = {}
        for j in range(i+1,n):
            x2,y2 = points[j]
            m = (y1-y2)/(x1-x2) if x1!=x2 else INFINITY
            if m not in counts: counts[m] = 1
            counts[m] += 1
        best = max(best, max(counts.values()))
    print(best)