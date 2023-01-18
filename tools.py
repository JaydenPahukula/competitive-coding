
def gcd(a:int, b:int):
    while(b):
       a, b = b, a % b
    return abs(a)

def phi(n:int):
    bigList = [True for i in range(1, n+2)]
    for i in range(2, n+1):
        if n % i == 0:
            for j in range(i, n+1, i):
                bigList[j] = False
    return bigList.count(True) - 1

def isPermutation(n1:int, n2:int):
    s = str(n1)
    if len(s) != len(str(n2)):
        return False

    d = {}
    for c in str(n2):
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    
    for c in s:
        if c not in d:
            return False
        d[c] -= 1
        if d[c] < 0:
            return False
    return True

def isPrime(n:int):
    #only works up to 3 * 10^14
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    c = 5;            
    while c ** 2 <= n:
        if n % c == 0: return False
        if n % (c + 2) == 0: return False
        c += 6
    return True

def findPrimes(n:int):
    primes = []
    nums = [True] * n
    for i in range(2, n):
        if nums[i]:
            primes.append(i)
            for j in range(i*i,n,i):
                nums[j] = False
    return primes

def RNtoDEC(s:str):
    num = 0
    tracker = 0
    for c in s[::-1]:
        if c == 'I':
            if tracker == 0:
                num += 1
            else:
                num -= 1
        elif c == 'V':
            num += 5
            tracker = max([tracker, 1])
        elif c == 'X':
            if tracker <= 2:
                num += 10
            else:
                num -= 10
            tracker = max([tracker, 2])
        elif c == 'L':
            num += 50
            tracker = max([tracker, 3])
        elif c == 'C':
            if tracker <= 4:
                num += 100
            else:
                num -= 100
            tracker = max([tracker, 4])
        elif c == 'D':
            num += 500
            tracker = max([tracker, 5])
        elif c == 'M':
            num += 1000
            tracker = max([tracker, 6])
        else:
            return "invalid input"

    return num

def DECtoRN(num:int):
    s = ""
    while num >= 1000:
        s += "M"
        num -= 1000
    if num >= 900:
        s += "CM"
        num -= 900
    if num >= 500:
        s += "D"
        num -= 500
    elif num >= 400:
        s += "CD"
        num -= 400
    while num >= 100:
        s += "C"
        num -= 100
    if num >= 90:
        s += "XC"
        num -= 90
    if num >= 50:
        s += "L"
        num -= 50
    elif num >= 40:
        s += "XL"
        num -= 40
    while num >= 10:
        s += "X"
        num -= 10
    if num == 9:
        s += "IX"
        return s
    if num >= 5:
        s += "V"
        num -= 5
    elif num == 4:
        s += "IV"
        return s
    while num > 0:
        s += "I"
        num -= 1
    return s


