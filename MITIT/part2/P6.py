MOD = 10**9+7

n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]

print(a[0][1]-a[0][0]+1)