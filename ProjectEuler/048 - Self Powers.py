

def findSelfPowers(n:int):
    s = 0
    for i in range(1, n+1):
        s += i ** i
    return str(s)[-10:]

print(findSelfPowers(1000))