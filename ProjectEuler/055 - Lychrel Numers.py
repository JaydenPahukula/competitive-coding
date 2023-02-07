
#checks if input is a palindrome
def isPalindrome(input):
    n = str(input)
    for i in range(round(len(n)/2)):
        if n[i] != n[-i-1]:
            return False
    return True

#returns int with digits reversed
def reverse(num:int):
    string = str(num)
    reverseString = ''
    for c in string:
        reverseString = c + reverseString
    return int(reverseString)

#find the amount of lychrel numbers below n
def lychrelNumbers(n):
    numLNs = 0
    for x in range(1,n):
        num = x
        i = 0
        while 1:
            num += reverse(num)
            if isPalindrome(num):
                break
            i += 1
            if i == 50:
                numLNs += 1
                break
    return numLNs

print(lychrelNumbers(10000))