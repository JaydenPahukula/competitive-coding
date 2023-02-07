
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2,int(num/2+1)):
        if num % i == 0:
            return False
    return True

def isTruncatable(num:int):
    s = str(num)
    for i in range(len(s)-1):
        if not isPrime(int(s[i+1:])) or not isPrime(int(s[:-i-1])):
            return False
    return True

def findTruncatablePrimes(N):
    total = 0
    numTPs = 0
    i = 11
    while 1:
        if isPrime(i) and isTruncatable(i):
            print("found truncatable prime!", i)
            total += i
            numTPs += 1
            print("numTPs =", numTPs)
            if numTPs >= N:
                break
        i += 2
    return total

print(findTruncatablePrimes(11))