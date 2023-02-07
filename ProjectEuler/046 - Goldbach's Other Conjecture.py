
def findPrimes(n):
    primes = []
    nums = [True] * n
    for i in range(2, n):
        if nums[i]:
            primes.append(i)
            for j in range(i*i,n,i):
                nums[j] = False
    return primes


n = 1
fail = False
l = []
primes = findPrimes(10000)
while 1:
    n += 2
    for x in l:
        if n % x == 0:
            fail = True
            break
    if not fail:
        l.append(n)
        continue
    else:
        fail = False
    for square in range(10000):
        for prime in primes:
            if n == prime + (2 * (square ** 2)):
                fail = True
                break
        if fail:
            break
    if fail:
        fail = False
        continue
    break
print(n)


    
    