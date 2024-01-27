for _ in range(int(input())):
    n, x = map(int, input().split())
    d = [False for _ in range(1000)]
    for a in map(int, input().split()):
        d[a-1] = True
    for v in range(1000):
        if not d[v]:
            if not x: break
            x -= 1
    print(v)