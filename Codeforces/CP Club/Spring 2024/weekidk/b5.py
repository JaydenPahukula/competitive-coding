import sys
input=sys.stdin.readline

def idk():
    n = int(input())
    cols = {}
    end = -1
    for _ in range(n):
        x,y = map(int, input().split())
        end = max(end, x)
        if x in cols:
            cols[x][0] = min(cols[x][0], y)
            cols[x][1] = max(cols[x][1], y)
        else:
            cols[x] = (y,y)
    x = 0
    y = 0
    while x < end:
        

    


out = []
for _ in range(int(input())):
    result = idk()
    if result:
        out.append("YES")
        out.append(result)
    else:
        out.append("NO")


print("\n".join(map(str, out)))
