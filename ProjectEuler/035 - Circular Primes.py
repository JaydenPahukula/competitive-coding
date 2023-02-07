
def findPrimes(n):
    primes = []
    nums = [True] * n
    for i in range(2, n):
        if nums[i]:
            primes.append(i)
            for j in range(i*i,n,i):
                nums[j] = False
    return primes

def rotate(s:str):
    out = ""
    for i in range(1,len(s)):
        out += s[i]
    out += s[0]
    return out  
        
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2,int(num/2+1)):
        if num % i == 0:
            return False
    return True

def numCircularPrimes1(primes):
    numCPs = 0
    CPs = []
    for prime in primes:
        s = str(prime)
        print("s = "+ s)
        fail = False
        rotatedPrime = 0
        for i in range(len(s)-1):
            rotatedPrime = int(rotate(s))
            #print("   ", rotatedPrime)
            if not isPrime(rotatedPrime):
                fail = True
                break
            elif prime != rotatedPrime and rotatedPrime in primes:
                #print("removing", rotatedPrime)
                primes.remove(rotatedPrime)
        if not fail:
            if prime == rotatedPrime: #e.g. 11
                numCPs += 1
            else:
                numCPs += len(s)
            #print("success!\n")
    return numCPs


def numCircularPrimes(N):
    #build list of nums
    nums = [2, 3, 5]
    for n in range(7,N):
        if str(n)[-1] not in ['0','2','4','5','6','8']:
            nums.append(n)
    
    numCPs = 0
    while 1:
        if len(nums) == 0:
            break

        s = str(nums[0])
        #print("\ns = " + s)
        #if only 1 digit or repeating digit (11)
        if len(s) == 1 or s == rotate(s):
            if isPrime(nums[0]):
                numCPs += 1
                #print("    success! numCPs =", numCPs)
            nums.pop(0)
            #print("    --")
            continue

        l = [nums[0]]
        if not isPrime(nums[0]):
            fail = True
        else:
            fail = False
        for j in range(len(s)-1):
            s = rotate(s)
            #print("    " + s)
            if not fail and not isPrime(int(s)):
                fail = True
            if int(s) in nums: nums.remove(int(s))
        if not fail:
            numCPs += len(s)
            #print("    success! numCPs =", numCPs)
        nums.pop(0)

    return(numCPs)


print(numCircularPrimes(1000000))

# tried:
# 70797