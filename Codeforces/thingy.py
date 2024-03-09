h,w=map(int,input().split())
a=[input().split()for _ in range(h)]
b=[input().split()for _ in range(h)]
print(("Yes","No")[sum([sum([a[y][x]^b[y][x]for y in range(h)])%2 for x in range(w)]+[sum([a[y][x]^b[y][x]for x in range(w)])%2 for y in range(h)])>0])
