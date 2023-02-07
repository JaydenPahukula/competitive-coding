
def findPrimes(n:int):
    primes = []
    nums = [True] * n
    for i in range(2, n):
        if nums[i]:
            primes.append(i)
            for j in range(i*i,n,i):
                nums[j] = False
    return primes

def solution(n:int):

    primes = findPrimes(10000)
    found = []
    maxa = int((n-(2**3)-(2**4))**(1/2))
    maxb = int((n-(2**2)-(2**4))**(1/3))
    maxc = int((n-(2**2)-(2**3))**(1/4))

    for a in [x for x in primes if x < maxa]:
        for b in [x for x in primes if x < maxb]:
            for c in [x for x in primes if x < maxc]:

                num = (a**2) + (b**3) + (c**4)
                if num < n:
                    found.append(num)

    return len([*set(found)])

print(solution(5*10**7))