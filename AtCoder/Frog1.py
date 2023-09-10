n = int(input())
h = list(map(int, input().split()))
c = [0 for _ in range(n)]
c[1] = abs(h[0]-h[1])
for i in range(2,n):
    c[i] = min(c[i-2]+abs(h[i]-h[i-2]), c[i-1]+abs(h[i]-h[i-1]))
print(c[n-1])