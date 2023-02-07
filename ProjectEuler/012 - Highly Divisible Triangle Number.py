import math

def numDivisors(n):
    divisors = 0
    for i in range(1,round(math.sqrt(n))):
        if n % i == 0:
            divisors += 2
    return divisors

def highlyDivisibleTriangleNumber(n):
    i = 2
    triangleNumber = 1

    while 1:
        if numDivisors(triangleNumber) >= n:
            return triangleNumber
        triangleNumber += i
        i += 1

print(highlyDivisibleTriangleNumber(500))
