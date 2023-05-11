DEFAULT = 200001
for _ in range(int(input())):
    n = int(input())
    minBoth = DEFAULT
    min1 = DEFAULT
    min2 = DEFAULT
    for _ in range(n):
        t, skills = map(int, input().split())
        if skills == 11 and t < minBoth:
            minBoth = t
        elif skills == 10 and t < min1:
            min1 = t
        elif skills == 1 and t < min2:
            min2 = t
    if minBoth != DEFAULT and min1 != DEFAULT and min2 != DEFAULT:
        print(min(minBoth, min1 + min2))
    elif minBoth != DEFAULT:
        print(minBoth)
    elif min1 != DEFAULT and min2 != DEFAULT:
        print(min1 + min2)
    else:
        print("-1")