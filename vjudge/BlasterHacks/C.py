n = int(input())
a = [-1 for _ in range(n)]
for i, x in enumerate(map(int, input().split())):
    a[x-1] = i+1
print(" ".join(map(str, a)))
