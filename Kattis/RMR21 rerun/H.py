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

a, b = map(int, input().split())
if isPrime(a) and isPrime(b) and a != b:
    print("full credit")
else:
    seen = set()
    for factor in primeFactors(a)+primeFactors(b):
        if factor in seen:
            print("no credit")
            break
        seen.add(factor)
    else:
        print("partial credit")