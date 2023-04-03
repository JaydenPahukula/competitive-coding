
def numSevens(num:int):
    if num < 7: return 0
    if num < 14: return 1
    s = str(num)
    n = len(s)
    leadingDigit = int(s[0])
    tempnum = 10**(n-1)
    temptotal = 0
    for i in range(n-1):
        temptotal += (9**i) * (10**(n-2-i))
    if leadingDigit < 7:
        return (temptotal * leadingDigit) + (numSevens(num-tempnum*leadingDigit))
    elif leadingDigit == 7:
        return (temptotal * 7) + (num-tempnum*leadingDigit+1)
    else:
        return (temptotal * (leadingDigit-1)) + tempnum + (numSevens(num-tempnum*leadingDigit))

a, b = map(int, input().split())
print(numSevens(b)-numSevens(a-1))