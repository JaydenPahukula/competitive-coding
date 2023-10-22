N,D,S = map(int, input().split())
land = sorted([int(input()) for _ in range(N)])

x = [[l,l] for l in land]
for i in range(1,N):
    x[i][0] += x[i-1][1]
