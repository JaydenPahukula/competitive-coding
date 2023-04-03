import sys

sys.stdin=open("milkvisits.in","r")
sys.stdout=open("milkvisits.out","w")

n, m = map(int, input().split())
breed = input()
farm = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    farm[a-1].append(b-1)
    farm[b-1].append(a-1)

for _ in range(m):
    start, end, preference = input().split()
    start = int(start)-1
    end = int(end)-1

    q = [(start, -1, {"G":False, "H":False})]
    while q:
        currFarm, lastFarm, foundBreed = q.pop()

        foundBreed[breed[currFarm]] = True

        if currFarm == end:
            if foundBreed[preference]:
                print('1', end='')
            else:
                print('0', end='')
            break

        for neighbor in farm[currFarm]:
            if neighbor != lastFarm:
                q.append((neighbor, currFarm, foundBreed.copy()))
