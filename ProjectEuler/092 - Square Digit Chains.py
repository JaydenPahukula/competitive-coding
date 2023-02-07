

N = 10000000
bigList = [0] * (N)
for i in range(N):
    bigList[i] = i

def find(n:int):
    if bigList[n] == n:
        return n
    bigList[n] = find(bigList[n])
    return bigList[n]

def solution():

    #configure bigList
    for i in range(N):
        temp = 0
        for c in str(i):
            temp += int(c)**2
        bigList[i] = temp
    bigList[1] = 1
    bigList[89] = 89
    
    #count all roots
    count = 0
    for i in range(N):
        if find(i) == 89:
            count += 1

    return count

print(solution())