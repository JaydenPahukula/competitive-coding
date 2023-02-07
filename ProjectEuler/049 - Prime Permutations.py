
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

def isPermutation(lits):
    for n in lits[1:]:
        s = str(lits[0])
        s1 = str(n)
        if len(s1) != len(s): return False
        for c in s1:
            if c not in s: return False
            s = s.replace(c, '', 1)
    return True

def findPrimePermutations():
    primes = findPrimes(10000)
    for a in primes:
        if len(str(a)) < 4: continue
        for diff in range(1, 10000 - a):
            b = a + diff
            c = a + diff + diff
            if len(str(b)) > 4 or len(str(c)) > 4: continue
            if not isPrime(b) or not isPrime(c): continue
            if not isPermutation([a, b, c]): continue
            print([a, b, c])
    return


findPrimePermutations()