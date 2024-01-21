from math import ceil
n, m = map(int, input().split())
miss = 0
for _ in range(n):
    t,a = map(int, input().split())
    miss = max(miss, ceil((m-t)/a))
print(miss+1)