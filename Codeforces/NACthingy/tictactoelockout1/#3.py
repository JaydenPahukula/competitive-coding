n = int(input())
a = [0]
b = [0]
d = -1
mn = 10**10
mx = 0
for x in map(int, input().split()):
    for _ in range(x):
        a.append(a[-1]+d)
        b.append(d)
        mn = min(mn,a[-1])
        mx = max(mx,a[-1])
    d = -d
for i in range(len(a)):
    a[i] -= mn
    if b[i] == 1: a[i] -= 1
for y in range(mx-mn+1):
    for x in range(1,len(a)):
        if a[x] == y:
            print("/" if b[x] == -1 else "\\",end="")
        else:
            print(" ",end="")
    print()
