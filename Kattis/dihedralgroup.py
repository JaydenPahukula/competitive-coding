n,m = map(int,input().split())
a = list(map(int, input().split()))*2
b = list(map(int, input().split()))
for i in range(n):
    for j in range(m):
        if a[i+j] != b[j]: break
    else:
        print(1)
        break
else:
    for i in range(n):
        for j in range(m):
            if a[i+j] != b[m-1-j]: break
        else:
            print(1)
            break
    else:
        print(0)
