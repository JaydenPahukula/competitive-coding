import math

def hcf(a:int, b:int):
    while(b):
       a, b = b, a % b
    return abs(a)

def solution(n:int, d1:int, d2:int):
    count = 0
    for d in range(5, n+1):
        n = math.ceil(d/3)
        while n/d < 1/d2:
            if hcf(n, d) == 1:
                count += 1
            n += 1
    return count

print(solution(12000, 3, 2))