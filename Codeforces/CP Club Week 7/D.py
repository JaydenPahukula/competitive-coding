import sys
input = sys.stdin.readline

output = []
for _ in range(int(input())):
    n = int(input())
    l = sorted(list(map(int, input().split())))
    numGroups = 0
    currMax,currSize = 0,0
    for x in l:
        currMax = max(x, currMax)
        currSize += 1
        if currSize >= currMax:
            numGroups += 1
            currMax,currSize = 0,0
    output.append(str(numGroups))
print("\n".join(output))