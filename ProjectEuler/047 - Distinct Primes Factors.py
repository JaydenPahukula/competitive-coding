
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2,int(num/2+1)):
        if num % i == 0:
            return False
    return True


def findPrimes(n:int):
    primes = []
    nums = [True] * n
    for i in range(2, n):
        if nums[i]:
            primes.append(i)
            for j in range(i*i,n,i):
                nums[j] = False
    return primes
primes = findPrimes(100000)


def primeFactorization(num:int):
    l = {}
    while 1:
        for prime in primes:
            if num % prime == 0:
                num /= prime
                if prime in l:
                    l[prime] += 1
                else:
                    l.update({prime:1})
                break
        if num == 1:
            return l




def findConsecutivePrimeFactors(f:int):
    num = 15
    used = []
    m = 0
    fail = False
    while 1:
        #input()
        if isPrime(num + m):
            num += m + 1
            m = 0
            continue
        factors = primeFactorization(num + m)
        if len(factors) != f:
            num += m + 1
            m = 0
            continue
        for n in factors:
            if [n, factors[n]] in used:
                fail = True
                break
            used.append([n, factors[n]])
        if fail:
            used = []
            fail = False
            num += 1 + m
            m = 0
            continue
        m += 1
        if m == f:
            out = []
            for i in range(f):
                out.append(num+i)
            return out
            


print(findConsecutivePrimeFactors(4))