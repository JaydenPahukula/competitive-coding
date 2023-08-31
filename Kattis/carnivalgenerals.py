from collections import deque

n = int(input())
no = [set() for _ in range(n)]
for general in range(1, n):
    ranking = list(map(int, input().split()))
    for num in ranking[(len(ranking)-1)//2+1:]:
        no[general].add(num)

front = 0
back = 0
line = deque([0])
unused = {x for x in range(1, n)}
for _ in range(n-1):
    print(line)
    validFront = [x for x in unused if x != front and front not in no[x] and x not in no[front]]
    if validFront:
        front = validFront[0]
        line.append(front)
        unused.remove(front)
        continue
    validBack = [x for x in unused if x != back and back not in no[x] and x not in no[back]]
    back = validBack[0]
    line.appendleft(back)
    unused.remove(back)
print(line)

    