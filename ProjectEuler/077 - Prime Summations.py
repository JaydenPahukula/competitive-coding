
def findPrimes(n:int):
    primes = []
    nums = [True] * n
    for i in range(2, n):
        if nums[i]:
            primes.append(i)
            for j in range(i*i,n,i):
                nums[j] = False
    return primes

def solution(TARGET:int):
    primes = findPrimes(100)
    n = 2

    while 1:
        ways = [0 for i in range(n+1)]
        ways[0] = 1

        for i in range(len(primes)):                
            for j in range(primes[i], n+1):
                ways[j] += ways[j - primes[i]]

        if ways[n] >= TARGET:
            break
        else:
            n += 1

    return n

print(solution(5000))