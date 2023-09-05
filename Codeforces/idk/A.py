for _ in range(int(input())):
    n = int(input())
    s = input()
    i = 0
    while i < n and s[i] == "P": i += 1
    currCount = 0
    maxCount = 0
    while i < n:
        if s[i] == "P":
            currCount += 1
        else:
            maxCount = max(maxCount, currCount)
            currCount = 0
        i += 1
    maxCount = max(maxCount, currCount)
    print(maxCount)