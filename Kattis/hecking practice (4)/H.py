n, l, p = map(int, input().split())
cars = [0 for _ in range(n)]
maxDistance = 0
for _ in range(p):
    x = int(input())
    distance = abs(((x//l)*l + l//2) - x)
    if x < l//2:
        distance = abs(x - l//2)
    elif x >= n*l:
        distance = x - (n*l) + l//2
    if distance > maxDistance: maxDistance = distance
    cars[min(x//l, n-1)] += 1
print(maxDistance)
print(max(cars))