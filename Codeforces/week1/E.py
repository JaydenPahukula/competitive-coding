n, m = map(int, input().split())
h = [0 for _ in range(n)]
for x in map(int, input().split()):
    h[x-1] += 1
print(min(h))