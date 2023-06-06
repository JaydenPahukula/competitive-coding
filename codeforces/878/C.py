for _ in range(int(input())):
    n, k, q = map(int, input().split())
    a = [int(x) for x in input().split()]
    numways = 0
    streak = 0
    for i in range(n):
        if a[i] <= q:
            streak += 1
        else:
            streak = 0

        if streak >= k:
            numways += streak-k+1
    print(numways)