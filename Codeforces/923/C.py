def check(a,b,k):
    countA = 0
    countB = 0
    countBoth = 0
    for i in range(1,k+1):
        if i in a and i in b:
            countBoth += 1
        elif i in a:
            countA += 1
        elif i in b:
            countB += 1
        else:
            return "NO"
    if countA > countB+countBoth:
        return "NO"
    if countB > countA+countBoth:
        return "NO"
    return "YES"


for _ in range(int(input())):
    n,m,k = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    print(check(a,b,k))
