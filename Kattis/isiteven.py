N, K = map(int, input().split())
a = [int(input()) for _ in range(N)]
for i in range(1,N):
    a[i] = a[i]*a[i-1] % 2**K
print(int(a[-1] % 2**K == 0))