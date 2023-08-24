t, b = map(int, input().split())
stock = list(map(int, input().split()))
version = {s: int(n) for s, n in [input().split() for _ in range(t)]}
for store in range(b):
    total = 0
    for item, currVersion in [input().split() for _ in range(stock[store])]:
        total += version[item] - int(currVersion)
    print(total)