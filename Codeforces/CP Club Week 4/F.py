for _ in range(int(input())):
    n = int(input())
    toRemove = [c=="0" for c in input()]
    seen = [False for i in range(n)]
    s = {i+1 for i in range(n) if toRemove[i]}
    s1 = {x for x in s}
    total = 0
    for i in range(n):
        for j in range(i, n, i+1):
            if j+1 not in s1: break
            if j+1 in s:
                s.remove(j+1)
                toRemove[j] = False
                total += i+1
    print(total)
