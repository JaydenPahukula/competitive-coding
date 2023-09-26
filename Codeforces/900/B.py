def firstNPrimes(n:int):
    primes = []
    nums = [True] * (20*n)
    i = 2
    while len(primes) < n:
        if nums[i]:
            primes.append(i)
            for j in range(i*i,20*n,i):
                nums[j] = False
        i += 1
    return primes

for _ in range(int(input())):
    print(" ".join(map(str, list(firstNPrimes(int(input())+2))[2:])))

