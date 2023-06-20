for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    total = 0
    numOperations = 0
    flipping = False
    for i in range(n):
        if a[i] > 0:
            flipping = False
            total += a[i]
        if a[i] < 0:
            if not flipping:
                flipping = True
                numOperations += 1
            total -= a[i]
    print(total, numOperations)