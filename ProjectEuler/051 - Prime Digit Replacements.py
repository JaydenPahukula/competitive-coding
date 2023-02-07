
def findPrimes(n:int):
    primes = []
    nums = [True] * n
    for i in range(2, n):
        if nums[i]:
            primes.append(i)
            for j in range(i*i,n,i):
                nums[j] = False
    return primes

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2,int(num/2+1)):
        if num % i == 0:
            return False
    return True

def masks(length:int):
    if length == 1:
        return [[1], [0]]
    l = []
    pattern = [False for i in range(length)]
    for m in masks(length-1):
        x = [1]
        x.extend(m)
        l.append(x)
        x = [0]
        x.extend(m)
        l.append(x)
    return l


def primeDigitReplacements(n):
    primes = findPrimes(1000000)[4:]
    checked = []
    #for each prime
    p = 0
    while 1:
        string = str(primes[p])

        #for each mask
        for mask in masks(len(string))[1:-1]:

            #last digit cannot be replaced
            if mask[-1] == 1:
                continue

            #apply the mask
            maskedString = ''
            for i in range(len(string)):
                if mask[i]:
                    maskedString += '*'
                else:
                    maskedString += string[i]

            #check for duplicates
            if maskedString in checked:
                continue
            else: checked.append(maskedString)

            #check each possible replacement digit
            score = 0
            for d in range(10):
                newString = maskedString.replace('*', str(d))
                if newString[0] == '0':
                    continue
                if isPrime(int(newString)):
                    score += 1
                    #win condition
                    if score >= n:
                        return(maskedString)
        
        p += 1


print(primeDigitReplacements(8))
#takes about 3 mins ^