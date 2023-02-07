
def findPrimes(n:int):
    primes = []
    nums = [True] * n
    for i in range(2, n):
        if nums[i]:
            primes.append(i)
            for j in range(i*i,n,i):
                nums[j] = False
    return primes

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

def check(p1:int, p2:int):
    if isPrime(int(str(p1)+str(p2))) and isPrime(int(str(p2)+str(p1))):
        return True
    return False

def primePairSets():
    primes = findPrimes(10000)
    for p1 in range(len(primes)-4):
        for p2 in range(p1+1, len(primes)-3):
            if not check(primes[p1], primes[p2]):
                continue
            for p3 in range(p2+1, len(primes)-2):
                if not check(primes[p2], primes[p3]) or not check(primes[p1], primes[p3]):
                    continue
                for p4 in range(p3+1, len(primes)-1):
                    if not check(primes[p3], primes[p4]) or not check(primes[p2], primes[p4]) or not check(primes[p1], primes[p4]):
                        continue
                    for p5 in range(p4+1, len(primes)):
                        if check(primes[p4], primes[p5]) and check(primes[p3], primes[p5]) and check(primes[p2], primes[p5]) and check(primes[p1], primes[p5]):
                            return sum([primes[p1], primes[p2], primes[p3], primes[p4], primes[p5]])
    return

print(primePairSets())