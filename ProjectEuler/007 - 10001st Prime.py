def isPrime(n):
    for i in range(2,round(n/2)+1):
        if n % i == 0:
            return False
    return True

i = 3
primeNumber = 1
while 1:
    if isPrime(i):
        primeNumber += 1
        print("found prime #"+str(primeNumber),"-",i)
        if primeNumber == 10001:
            quit()
    i += 2