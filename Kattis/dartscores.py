import math
for _ in range(int(input())): print(sum([int(10-max(0,r-0.000001)//20) for r in [math.hypot(*map(int, input().split())) for _ in range(int(input()))] if r <= 200]))