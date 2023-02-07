

def ToBinary(n:int):
    i = 1
    s = ""
    while 2**i <= n:
        i += 1
    i -= 1
    while i >= 0:
        if 2**i <= n:
            s += '1'
            n -= 2** i
        elif 2**i > n:
            s += '0'
        i -= 1
    return s

def isPalindrome(input):
    n = str(input)
    for i in range(round(len(n)/2)):
        if n[i] != n[-i-1]:
            return False
    return True

def findDBPs(N):
    total = 0
    for num in range(1,N+1):
        if isPalindrome(str(num)) and isPalindrome(ToBinary(num)):
            total += num
    return total

print(findDBPs(1000000))