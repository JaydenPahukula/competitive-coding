
def isPrime(n:int):
    #only works up to 3 * 10^14
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    c = 5;            
    while c ** 2 <= n:
        if n % c == 0: return False
        if n % (c + 2) == 0: return False
        c += 6
    return True

def spiralPrimes(ratio:float):
    i = 1
    increment = 2
    numPrimes = 0
    n = 1
    while 1:
        for x in range(4):
            i += increment
            if isPrime(i):
                numPrimes += 1
        n += 4
        if numPrimes / n < ratio:
            return increment + 1
        increment += 2
    return

print(spiralPrimes(0.1))

#tried
