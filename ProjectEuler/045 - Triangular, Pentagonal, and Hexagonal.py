import math

def isPentagonal(num:int):
    x = (math.sqrt(1 + 24 * num) + 1) / 6
    if x % 1 == 0:
        return True
    return False

def isHexagonal(num:int):
    x = (math.sqrt(1 + 8 * num) + 1) / 4
    if x % 1 == 0:
        return True
    return False

def findTriPentHexagonal():
    n = 1
    while 1:
        T = n * (n + 1) / 2
        if isPentagonal(T) and isHexagonal(T):
            print(int(T), "\nPress enter to find next...")
            input()
        n += 1
    
findTriPentHexagonal()