for _ in range(int(input())):
    n = int(input())
    s = [c == "1" for c in input()]
    f = [c == "1" for c in input()]
    add, remove = 0, 0
    for i in range(n):
        if s[i] and not f[i]:
            remove += 1
        elif not s[i] and f[i]:
            add += 1
    print(max(add, remove))
