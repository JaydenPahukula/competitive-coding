from collections import defaultdict

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

n = int(input())
hist = defaultdict(int)
for prime in primeFactors(n):
    hist[prime] += 1

print(max(hist,key=lambda x:hist[x]))
