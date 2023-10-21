n = int(input())
a = sorted([int(input()) for _ in range(n)])
dp = set([0])
for i in range(n):
    for item in list(dp):
        if item < 1000:
            dp.add(item+a[i])
print(min(dp, key=lambda x:abs(1000.1-x)))