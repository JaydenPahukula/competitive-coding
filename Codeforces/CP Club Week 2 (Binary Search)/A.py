for _ in range(int(input())):
    n, k = map(int, input().split())
    mice = sorted([n-int(x) for x in input().split()])
    count = 0
    numMice = 0
    for m in mice:
        if count+m >= n: break
        numMice += 1
        count += m
    print(numMice)
