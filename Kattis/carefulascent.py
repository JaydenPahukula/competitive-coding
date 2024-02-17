x, y = map(int, input().split())
n = int(input())

# for _ in range(n):
#     start, stop, factor = map(float, input().split())
#     dist = stop-start
#     y = y - dist + (dist * factor)

# print(x/y)

sheilds = [tuple(map(float, input().split())), ]

lo, hi = 0,99**9
for _ in range(1000):
    m = (hi+lo)/2
