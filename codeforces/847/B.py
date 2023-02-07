numTestCases = int(input())
for _ in range(numTestCases):
    n, s, r = map(int, input().split())
    a = [1 for i in range(n-1)]
    a[0] += r-n+1
    for i in range(n-1):
        if a[i] > s-r:
            a[i+1] += a[i]-s+r
            a[i] = s-r
    for dice in a:
        print(dice, end=' ')
    print(s-r, end=' \n')