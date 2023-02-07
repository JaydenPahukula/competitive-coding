def sumOfDigits(n):
    list = []
    string = str(n)
    for i in range(len(string)):
        list.append(int(string[i]))
    return sum(list)

def factorialDigitSum(n):
    sum = 1
    for i in range(1,n+1):
        sum *= i
    return sumOfDigits(sum)

print(factorialDigitSum(100))