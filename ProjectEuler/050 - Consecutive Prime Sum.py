
def findPrimes(n:int):
    primes = []
    nums = [True] * n
    for i in range(2, n):
        if nums[i]:
            primes.append(i)
            for j in range(i*i,n,i):
                nums[j] = False
    return primes

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2,int(num/2+1)):
        if num % i == 0:
            return False
    return True

def longestConsecutivePrimeSum(n:int):
    primes = findPrimes(n)
    cumulativePrimes = [0]
    maxdiff = 0
    maxp = 0
    s = 0
    for prime in primes:
        s += prime
        cumulativePrimes.append(s)

    for i in range(len(primes)):
        print(i)
        for j in range(i):
            x = cumulativePrimes[i] - cumulativePrimes[j]
            if x > n: continue
            if isPrime(x):
                if i - j > maxdiff:
                    maxdiff = i - j
                    maxp = x
                break
    return maxp


print(longestConsecutivePrimeSum(1000000))