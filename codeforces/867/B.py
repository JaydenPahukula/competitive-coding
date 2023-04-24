for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    print(max(a[0]*a[1], a[-1]*a[-2]))