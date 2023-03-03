
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

def findPrimes(n:int):
    primes = []
    nums = [True] * n
    for i in range(2, n):
        if nums[i]:
            primes.append(i)
            for j in range(i*i,n,i):
                nums[j] = False
    return primes


