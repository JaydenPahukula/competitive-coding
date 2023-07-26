for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))

    mini = 0
    minj = 0
    minVal = 10000000000000
    for i in range(n-1):
        for j in range(i+1, n):
            val = l[i] ^ l[j]
            if val < minVal:
                minVal = val
                mini = i
                minj = j
    x = l[minj]^(2**k-1)
    y = l[mini]^(2**k-1)
    print("   ", mini+1, minj+1, x, y)
    print("   ", (mini^x)&(minj^x), (mini^y)&(minj^y))
        