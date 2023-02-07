

def isPalindrome(input):
    n = str(input)
    for i in range(round(len(n)/2)):
        if n[i] != n[-i-1]:
            return False
    return True

top = 0
for a in range(100,1000):
    for b in range(100,1000):
        if isPalindrome(a*b):
            if a*b > top:
                top = a*b
            
print(top)
