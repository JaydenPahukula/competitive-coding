for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    h = list(map(int, input().split()))

    subs = []

    i = 0
    sub = []
    while i < n-1:
        if h[i]/h[i+1] % 1 < 0.0001:
            sub = [a[i], a[i+1]]
            i += 1
            while i < n-1 and h[i]/h[i+1] % 1 == 0:
                sub.append(a[i+1])
                i += 1
            subs.append(sub)
            sub = []
        i += 1
    
    longest = 0
    for b in subs:
        n = len(b)
        start = 0
        end = 1
        runningSum = b[0]
        while start < n:
            while end < n and runningSum + b[end] <= k:
                runningSum += b[end]
                end += 1
            #print(start, end, runningSum, start-end)
            longest = max(longest, end - start)

            runningSum -= b[start]
            start += 1

    if longest:
        print(longest)
    elif min(a) <= k:
        print(1)
    else:
        print(0)