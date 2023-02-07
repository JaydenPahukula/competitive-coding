
def factorial(n:int):
    f = 1
    for i in range(1,n+1):
        f *= i
    return f

def findDigitFactorials(N):
    sum = 0
    for n in range(3,N):
        count = 0
        s = str(n)
        for c in s:
            count += factorial(int(c))
        if count == n:
            sum += n
    return sum

print(findDigitFactorials(10000000))