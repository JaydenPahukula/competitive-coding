for _ in range(int(input())):
    n, t = map(int, input().split())
    a = [int(x)+i for i, x in enumerate(input().split())]
    b = [int(x) for x in input().split()]
    c = sorted([(a[i], b[i], i) for i in range(n)], reverse=True)
    maxe = -1
    maxi = -1
    for i in range(n):
        if c[i][0] <= t and c[i][1] > maxe:
            maxe = c[i][1]
            maxi = c[i][2]+1
    print(maxi)