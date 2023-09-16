n = int(input())
l = sorted(list(map(int, input().split())))
print((n-1)//2)
print(" ".join([str(l[(0 if i%2 else n//2)+i//2]) for i in range(n)]))