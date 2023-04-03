import math

n, b = map(int, input().split())
print(int(math.log(n, b+1)+1))