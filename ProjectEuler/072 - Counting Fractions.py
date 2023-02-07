
def solution(n:int):
    bigList = [i for i in range(n+1)]
    count = 0
    for i in range(2, n+1):
        if bigList[i] == i:
            for j in range(i, n+1, i):
                bigList[j] *= 1 - 1 / i
        count += bigList[i]
    return int(count)

print(solution(1000000))