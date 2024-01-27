for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    l = []
    for x in a:
        for i in range(len(l)):
            if abs(x-l[i]) > 1:
                l[i] = x
                break
        else:
            l.append(x)
    print(len(l))