for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted([(int(x), i) for i, x in enumerate(input().split())])
    b = sorted(list(map(int, input().split())))
    c = [0] * n
    for i in range(n):
        c[a[i][1]] = b[i]
    print(' '.join(map(str, c)))