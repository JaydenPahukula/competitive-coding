import math

bigList = [0] * 10000000

def value(n:int):
    if bigList[n] == 0:
        s = 0
        for x in [int(c) for c in str(n)]:
            s += math.factorial(x)
        bigList[n] = s
        return s
    else:
        return bigList[n]

def solution(n:int, target:int):
    count = 0
    for i in range(1, n):
        chain = [i]
        next = value(i)
        while next not in chain:
            chain.append(next)
            next = value(next)
        if len(chain) == target:
            count += 1

    return count

print(solution(1000000, 60))