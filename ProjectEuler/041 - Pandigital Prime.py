


def findPrimes(n):
    primes = []
    nums = [True] * n
    for i in range(2, n):
        if nums[i]:
            primes.append(i)
            for j in range(i*i,n,i):
                nums[j] = False
    return primes

def nDigitPandigital(num):
    numlength = len(str(num))
    if numlength > 9 or '0' in str(num): return False
    l = []
    for i in range(numlength):
        l.append(i+1)
    for c in str(num):
        if int(c) not in l:
            return False
        l.remove(int(c))
    return numlength


def highestPandigitalPrime(n):
    primes = findPrimes(n)
    maxn = 0
    maxp = 0
    for prime in primes:
        x = nDigitPandigital(prime)
        if x >= maxn:
            maxn = x
            maxp = prime
    return maxp

print(highestPandigitalPrime(100000000))