n,k,q = map(int, input().split())
a = [0 for _ in range(n)]
for _ in range(q):
    a[int(input())-1] += 1
for i in range(n):
    if k+a[i]-q > 0:
        print("Yes")
    else:
        print("No")
