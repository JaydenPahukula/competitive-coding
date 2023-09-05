
def gcd(a:int, b:int):
    while(b):
       a, b = b, a % b
    return abs(a)

def phi(n:int):
    bigList = [True for i in range(1, n+2)]
    for i in range(2, n+1):
        if n % i == 0:
            for j in range(i, n+1, i):
                bigList[j] = False
    return bigList.count(True) - 1

def isPermutation(n1:int, n2:int):
    s = str(n1)
    if len(s) != len(str(n2)):
        return False

    d = {c: 0 for c in set(str(n2))}
    for c in str(n2):
        d[c] += 1
    
    for c in s:
        if c not in d: return False
        d[c] -= 1
        if d[c] < 0: return False
    return True

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

def primeFactors(n:int):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

import random
def isPrime(n):
    # Miller-Rabin primality test:
    # False - means n is certainly not prime.
    # True  - means n is very likely a prime.

    if n!=int(n):
        return False
    n=int(n)
    #Miller-Rabin test for prime
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
        
    if n==2 or n==3 or n==5 or n==7:
        return True
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)
  
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  
 
    for i in range(8):#number of trials 
        a = random.randrange(2, n)
        if trial_composite(a):
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


