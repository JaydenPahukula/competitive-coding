for _ in range(int(input())):
    n = int(input())
    attack = list(map(int, input().split()))
    defense = list(map(int, input().split()))
    left = list(range(n))
    right = list(range(n))
    alive = [True]*n

    def findLeft(x):
        if left[x] == x: return x
        if left[x] == -1: return -1
        else: left[x] = findLeft(left[x])
        return left[x]
    def findRight(x):
        if right[x] == x: return x
        if right[x] == -1: return -1
        else: right[x] = findRight(right[x])
        return right[x]
    
    out = []
    for i in range(n):
        damage = [0]*n
        for j in range(n):
            if not alive[j]: continue
            if j > 0:
                target = findLeft(j-1)
                if target != -1: damage[target] += attack[j]
            if j < n-1:
                target = findRight(j+1)
                if target != -1: damage[target] += attack[j]
        killCount = 0
        for j in range(n):
            if alive[j] and damage[j] > defense[j]:
                alive[j] = False
                if j == 0: left[j] = -1
                else: left[j] = left[j-1]
                if j == n-1: right[j] = -1
                else: right[j] = right[j+1]
                killCount += 1
        out.append(killCount)
    
    print(" ".join(map(str, out)))