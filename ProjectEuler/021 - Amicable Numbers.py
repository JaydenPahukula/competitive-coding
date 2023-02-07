def divisors(n):
    divisors = []
    for i in range(1,round(n/2+1)):
        if n % i == 0:
            divisors.append(i)
    return divisors

def sumOfAmicableNumbers(n):
    amicableNumbers = []
    for i in range(1,n+1):
        if i in amicableNumbers:
            continue
        x = sum(divisors(i))
        if sum(divisors(x)) == i and x != i:
            amicableNumbers.extend([i,x])
    return sum(amicableNumbers)
        

print(sumOfAmicableNumbers(10000))