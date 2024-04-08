import sys
from collections import defaultdict
input=sys.stdin.readline

out = []
for _ in range(int(input())):
    n,m,k = map(int, input().split())
    a = list(map(int, input().split()))
    b = defaultdict(int)
    for x in map(int, input().split()): b[x] += 1
    
    window = defaultdict(int)
    for x in a[:m]: window[x] += 1

    count = 0
    totalMatches = sum(min(window[x], b[x]) for x in window)

    if totalMatches >= k: count += 1
    for i in range(n-m):
        remove = a[i]
        window[remove] -= 1
        if window[remove] < b[remove]: totalMatches -= 1
        add = a[i+m]
        window[add] += 1
        if window[add] <= b[add]: totalMatches += 1
        if totalMatches >= k: count += 1
    
    out.append(count)

print("\n".join(map(str, out)))
