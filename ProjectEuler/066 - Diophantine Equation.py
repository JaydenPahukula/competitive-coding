import math
import mpmath as mp

#WIP

def diophantineEquation(n:int):
    maxX = 0
    maxD = 0
    for D in range(778, n+1):
        print("D =", D)

        #skip squares
        if math.sqrt(D) % 1 == 0:
            print("skipped")
            continue

        #find minimum x value
        x = 0
        y = 0.1
        while y != int(y) or y == 0:
            x += 1
            y = math.sqrt((x**2 - 1) / D)
        
        #check if max
        print(x, y)
        if x >= maxX:
            maxX = x
            maxD = D

        #input()

    return maxD

def diophantineEquation1(n:int):
    maxX = 0
    maxD = 0
    for D in range(1, n+1):
        print("D =", D, "------")

        #skip squares
        if math.sqrt(D) % 1 == 0:
            print("skipped")
            continue

        #find minimum x value
        x = 0.1
        y = 0
        while x != int(x):
            y += 1
            x = math.sqrt(1 + (D * y**2))

        z = x**2 - (D * y**2)
        print(x, y, z)

        if z != 1:
            continue
            print("redoing...")
            x = 0
            y = 0.1
            while y != int(y) or y == 0:
                x += 1
                y = math.sqrt((x**2 - 1) / D)

            z = x**2 - (D * y**2)
            print(x, y, z)


        
        #check if max
        if x >= maxX:
            maxX = x
            maxD = D

        #input()

    return maxD


print(diophantineEquation1(1000))