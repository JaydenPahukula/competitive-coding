import math

def nearestTriangleNumber(n:int):
    return int(1+math.sqrt(8*n+1))//2

def triangle(n:int):
    return n*(n+1)//2

for _ in range(int(input())):
    n = int(input())
    total = 0

    last = 0
    y = nearestTriangleNumber(n-1)
    x = n-triangle(nearestTriangleNumber(n-1)-1)
    d = y-x+1
    startingIncrement = y
    startingN = n
    for i in range(d):
        increment = startingIncrement
        n1 = startingN
        
        for _ in range(x):
            total += n1*n1
            n1 -= increment
            increment -= 1
        
        startingIncrement -= 1
        startingN -= startingIncrement
    
    print(total)
