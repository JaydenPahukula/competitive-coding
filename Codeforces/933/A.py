for _ in range(int(input())):
    n,m,k = map(int, input().split())
    ways = 0
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for a1 in a:
        for b1 in b:
            if a1+b1 <= k: ways += 1
    print(ways)