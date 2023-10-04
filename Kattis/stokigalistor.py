n = int(input())
l = list(map(int, input().split()))
ls = sorted(l)
print(sum([1 for i in range(n) if l[i] != ls[i]]))