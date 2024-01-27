from math import prod

n = int(input())
best = 0
for i in range(n//2,n+1):
    x = prod([int(c) for c in str(i)])
    best = max(best, x)
print(best)