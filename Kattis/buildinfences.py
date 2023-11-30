n = int(input())
ycoords = []
xcoords = []
for _ in range(n):
    x,y = map(int, input().split())
    xcoords.append(x)
    ycoords.append(y)

print(2 * (max(ycoords) - min(ycoords) + max(xcoords) - min(xcoords) + 4))