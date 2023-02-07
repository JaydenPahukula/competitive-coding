import math


def maxIntegerRightTriangle(N):
    maxs = 0
    maxp = 0
    for perimeter in range(1,N+1):
        solutions = 0
        for a in range(1, perimeter+1):
            for b in range(a, perimeter+1):
                c = math.sqrt((a**2)+(b**2))
                if c.is_integer() and a + b + c == perimeter:
                    solutions += 1
        if solutions > maxs:
            maxs = solutions
            maxp = perimeter
    return maxp

print(maxIntegerRightTriangle(1000))