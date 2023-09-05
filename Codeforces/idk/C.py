for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    if len(set(a)) == 1:
        print(-1)
    else:
        i = 1
        while i <= n and a[-i-1] == a[-1]: i += 1
        print(n-i, i)
        print(" ".join(map(str, a[:-i])))
        print(" ".join(map(str, a[-i:])))
