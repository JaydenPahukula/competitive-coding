for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    c = [0 for _ in range(n+1)]
    c1 = 0
    for num in l:
        if num == 1:
            c1 += 1
            continue
        x = num
        while x <= n:
            c[x] += 1
            x += num
    print(max(c)+c1)