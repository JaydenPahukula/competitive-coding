def numPrimeFactors(n:int):
    i = 2
    count = 0
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            count += 1
    if n > 1:
        count += 1
    return count

n = int(input())
print(numPrimeFactors(n))