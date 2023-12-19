for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(1,n):
        b[i] = max(b[i], b[i-1])
    
    score = 0
    runningSum = 0
    for i in range(min(n,k)):
        runningSum += a[i]
        score = max(score, runningSum+b[i]*(k-i-1))

    print(score)