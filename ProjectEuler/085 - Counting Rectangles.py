import math

def numRectangles(l:int, w:int):
    return (l * w * (l+1) * (w+1)) // 4

def solution(n:int):
    minx = 0
    miny = 0
    mindiff = n
    for x in range(1, math.ceil(math.pow(4*n, 1/4))+1):
        y = x
        last = 0
        num = numRectangles(x, y)
        while num < n:
            last = num
            num = numRectangles(x, y)
            y += 1
        if num - n < mindiff:
            mindiff = num - n
            minx = x
            miny = y - 1
        if  n - last < mindiff:
            mindiff = n - last
            minx = x
            miny = y - 2
        
    return minx * miny

print(solution(5000000))