
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
    primses = findPrimes(100)
    x = 1
    i = -1
    while x < n:
        i += 1
        x *= primses[i]
    x /= primses[i]
    
    return int(x)

print(solution(1000000))