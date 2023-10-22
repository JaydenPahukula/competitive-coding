n = int(input())
d = {}
for _ in range(n):
    for name in input().split(","):
        if name in d: d[name] += 1
        else: d[name] = 1
winner = max(d.keys(), key=lambda x:d[x])
print(winner)
print(d[winner])