
def isBouncy(n:int):
    isIncreasing = True
    isDecreasing = True
    s = str(n)
    for i in range(1, len(s)):
        if isIncreasing and s[i] < s[i-1]:
            isIncreasing = False
        if isDecreasing and s[i-1] < s[i]:
            isDecreasing = False
        if not isIncreasing and not isDecreasing:
            return True
    return False

def solution(target:float):
    n = 1
    bouncyCount = 0
    while 1:
        if isBouncy(n):
            bouncyCount += 1
            if bouncyCount/n == target:
                return n
        n += 1
    return

print(solution(0.99))