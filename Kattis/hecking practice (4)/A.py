n, c = map(int, input().split())
w = list(map(int, input().split()))
if n > 1:
    count = [0 for _ in range(n+1)]
    count[0] = -1
    s = 0
    e = 0
    t = 0
    windowSum = w[0] + w[1]
    while s < n:
        if e+2 > n or windowSum > c:
            if s <= e:
                count[s] = t - count[s]
            windowSum -= w[s]
            s += 1
        else:
            e += 1
            if e >= s:
                count[e] = t
            if e+1 < n:
                windowSum += w[e+1]
        
        t += 1
    print("\n".join(map(str, count[:-1])))
else:
    print("1")