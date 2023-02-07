digits = [0,1,2,3,4,5,6,7,8,9]
length = len(digits)
pfinal = 1000000
p = 1
digit = 0

def swap(l,a,b):
    c = l[a]
    l[a] = l[b]
    l[b] = c
    return l

def factorial(n):
    f = 1
    for i in range(2,n+1):
        f = f * i
    return f


i = 0
while 1:
    print(digits)
    if p == pfinal:
        print("hooray!")
        break
    if factorial(length-1-digit) + p > pfinal:
        print("switching digits " + str(digit) + " and " + str(digit+1+i) + " wont work... moving on")
        i = 0
        digit += 1
    else:
        print("switching digits " + str(digit) + " and " + str(digit+1+i) + "...")
        digits = swap(digits,digit,digit+1+i)
        p += factorial(length-1-digit)
        i += 1
        print("now at permutation #" + str(p))