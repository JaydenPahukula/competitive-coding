for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    d = {x:[] for x in set(a)}
    total = {x:0 for x in d}
    for i in range(n):
        d[a[i]].append(b[i])
        total[a[i]] += b[i]

    for x in d:
        l = sorted(d[x])
        for i in range(1,len(l)): l[i]+=l[i-1]
        d[x] = l

    for k in range(1,n+1):
        print(sum([total[team]-(d[team][len(d[team])%k-1] if (len(d[team])%k-1)!=-1 else 0) for team in d]), end=" ")
    print()