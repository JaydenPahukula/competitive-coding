x, y = map(int, input().split())
n = int(input())

for _ in range(n):
    start, stop, factor = map(float, input().split())
    dist = stop-start
    y = y - dist + (dist * factor)

print(x/y)