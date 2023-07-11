
n = int(input())
xlist = [0 for _ in range(n)]
ylist = [0 for _ in range(n)]
for _ in range(n):
    x, y = map(int, input().split(' '))
    xlist[x-1] += 1
    ylist[y-1] += 1

count = 0
for list in [xlist, ylist]:
    holes = [num for num in range(n-1, -1, -1) if list[num] == 0]
    for num in range(n):
        for i in range(max(0, list[num]-1)):
            hole = holes.pop()
            count += abs(num-hole)
        list[num] = min(list[num], 1)

print(count)