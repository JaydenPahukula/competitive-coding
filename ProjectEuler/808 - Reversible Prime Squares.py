import math

#finds all primes below n
def findPrimes(n:int):
    primes = []
    nums = [True] * n
    for i in range(2, n):
        if nums[i]:
            primes.append(i)
            for j in range(i*i,n,i):
                nums[j] = False
    return primes
    if num <= 1:
        return False
    for i in range(2,int(num/2+1)):
        if num % i == 0:
            return False
    return True

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2,int(num/2+1)):
        if num % i == 0:
            return False
    return True

def reversiblePrimeSquares(n:int):
    primes = findPrimes(20000000)
    RPSs = []
    i = len(primes)
    for prime in primes:
        i -= 1
        r = int(str(prime**2)[::-1])
        if r != prime**2 and math.sqrt(r) % 1 == 0 and isPrime(math.sqrt(r)):
            RPSs.append(prime**2)
            RPSs.append(r)
            primes.remove(math.sqrt(r))
            if len(RPSs) >= n:
                return sum(RPSs)
    return


print(reversiblePrimeSquares(50))


# tried:
# 36854889426530
# 34740767840240
