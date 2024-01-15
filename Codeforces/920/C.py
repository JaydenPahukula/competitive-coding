for _ in range(int(input())):
    n,f,a,b = map(int, input().split())
    m = list(map(int, input().split()))
    t = 0
    for i in range(n):
        d = m[i]-t
        f -= min(b, d*a)
        if f <= 0: break
        t += d
    else:
        print("YES")
        continue
    print("NO")
