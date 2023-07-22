# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     numWays = 0
#     for i in range(min(2**k, n+1)):
#         mask = list(map(int, bin(i)[:1:-1].ljust(k, '0')))
#         cost = sum([2**i for i in range(k) if mask[i]])
#         #print(i, [l[i] for i in range(k) if mask[i]], mask, cost)
#         if cost > n:
#             break
#         numWays += 1
#     print(numWays)

import math

for _ in range(int(input())):
    n, k = map(int, input().split())
    if math.log2(n) < k:
        print(n+1)
    else:
        print(2**k)