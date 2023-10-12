
# l = []
# mem = {}
# def minOps(i):
#     global count
#     print(count)
#     count += 1
#     if i > len(l): return 10**7
#     if i == len(l): return 0
#     if i not in mem:
#         mem[i] = min(minOps(i+1)+1, minOps(i+l[i]+1))
#     return mem[i]

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    dp = [10**6 for _ in range(n)]+[0]
    for i in range(n-1, -1, -1):
        x1,x2 = 10**6, 10**6
        if i < n: x1 = dp[i+1]+1
        if i < n-l[i]: x2 = dp[i+l[i]+1]
        dp[i] = min(x1, x2)
    print(dp[0])