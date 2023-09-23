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

def findPrimes(n:int):
    primes = []
    nums = [True] * n
    for i in range(2, n):
        if nums[i]:
            primes.append(i)
            for j in range(i*i,n,i):
                nums[j] = False
    return primes

n = int(input())
primedict = {}
for prime in findPrimes(n+1):
    primedict[prime] = set([x for x in range(prime,n+1,prime)])

p,q = 0,1
for k in range(2,n+1):
    # count = 0
    # #print(k, "====")
    # for j in range(2, k+1):
    print([primedict[s] for s in primeFactors(k)])
    count = len(set().union([primedict[s] for s in primeFactors(k)]))
    if count/k > p/q:
        p = count
        q = k
print(p/q, p, q)