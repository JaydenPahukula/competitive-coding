n = int(input())
teams = [tuple(map(int, input().split())) for _ in range(n)]

def checkTeam(i:int):
    minB = min([b for a,b in teams[i:i+3]])
    maxA = max([a for a,b in teams[i:i+3]])
    return maxA > i and minB <= i+2

i = 0
count = 0
while i < n-2:
    if checkTeam(i):
        count += 1
        i += 3
    else:
        i += 1
print(count)

"""

7
1 3
1 3
1 4
2 5
2 6
2 6
5 6


"""