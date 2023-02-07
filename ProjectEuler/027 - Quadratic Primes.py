
DEBUG = False
ARANGE = 999
BRANGE = 1000

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2,int(num/2+1)):
        if num % i == 0:
            return False
    return True


primes = []
for i in range(2, 100000):
    if isPrime(i):
        primes.append(i)
print("found primes")

bprimes = []
for p in primes:
    if p > BRANGE:
        break
    bprimes.append(-p)
    bprimes.append(p)
print("found bprimes\ncalculating...")
    

nmax = 0
amax = 0
bmax = 0
for a in range(-ARANGE,ARANGE+1):
    print(a)
    for b in bprimes:
        if DEBUG: print("a =", a, "  b =", b)
        n = 0
        while 1:
            if (n**2)+(a*n)+b not in primes:
                if DEBUG: print("failed at", n)
                break
            else:
                n += 1
        if n > nmax:
            if DEBUG: print("new record!----------")
            nmax = n
            amax = a
            bmax = b
print(amax * bmax)