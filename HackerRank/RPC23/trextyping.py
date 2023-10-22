from math import sqrt
from collections import defaultdict
A = [0]*4 + [1]*12 + [sqrt(2)]*8 + [2]*10 + [sqrt(5)]*12 + [sqrt(8)]*4 + [3]*10 + [sqrt(10)]*12 + [sqrt(13)]*8 + [sqrt(18)]*4

count = defaultdict(int)
s = input()
for c in s:
    if c.isupper(): count["SHIFT"] += 1
    count[c.lower()] += 1

print(2*sum([A[i]*count for i,count in enumerate(sorted(count.values(),reverse=True))]))