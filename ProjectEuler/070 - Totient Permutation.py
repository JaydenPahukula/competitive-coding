import math

def findPrimes(n:int):
    primes = []
    nums = [True] * n
    for i in range(2, n):
        if nums[i]:
            primes.append(i)
            for j in range(i*i,n,i):
                nums[j] = False
    return primes

def isPermutation(n1:int, n2:int):
    s = str(n1)
    if len(s) != len(str(n2)):
        return False

    d = {}
    for c in str(n2):
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    
    for c in s:
        if c not in d:
            return False
        d[c] -= 1
        if d[c] < 0:
            return False
    return True

def solution(N:int):
    primes = findPrimes(N)
    minRatio = 1000
    minn = 0
    for i in range(1, len(primes)):
        for j in range(i+1, len(primes)):
            n = primes[i] * primes[j]
            if n > N:
                break
            p = (primes[i]-1) * (primes[j]-1)
            if isPermutation(n, p) and (n/p) < minRatio:
                minRatio = n/p
                minn = n
    return minn

print(solution(10**7))


