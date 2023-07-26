for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    startColor = l[0]
    endColor = l[-1]
    if startColor == endColor:
        count = 0
        for i in range(n):
            if l[i] == startColor: count += 1
        if count >= k:
            print("YES")
        else:
            print("NO")
    else:
        startColorCount = 1
        endColorCount = 1
        for i in range(1, n-1):
            if startColorCount < k:
                if l[i] == startColor:
                    startColorCount += 1
            else:
                if l[i] == endColor:
                    endColorCount += 1
        if endColorCount >= k:
            print("YES")
        else:
            print("NO")