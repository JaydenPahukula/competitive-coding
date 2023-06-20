for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    cost = 0
    for i in range(n//2):
        cost += a[-1-i] - a[i]
    print(cost)