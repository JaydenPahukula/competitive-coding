for _ in range(int(input())):
    n, k = map(int, input().split())
    l = sorted(list(map(int, input().split())))
    groups = []
    c = 1
    for i in range(1, n):
        if l[i] - l[i-1] > k:
            groups.append(c)
            c = 1
        else:
            c += 1
    groups.append(c)
    print(sum(sorted(groups)[:-1]))
