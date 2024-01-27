from math import ceil
k,n,s,p = map(int, input().split())
print(ceil(ceil(n/s)*k/p))
