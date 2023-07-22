for _ in range(int(input())):
    n, c = map(int, input().split())
    a = sorted([int(x)+i+1 for i, x in enumerate(input().split())])
    i = 0
    score = 0
    while i < len(a) and c-a[i] >= 0:
        c -= a[i]
        i += 1
        score += 1
    print(score)

