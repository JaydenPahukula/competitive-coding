n, mn, mx = map(int, input().split())
f = [0] * n
for i in range(n):
    f[i] = int(input())
f.sort()

for i in range(1, n):
    if f[i] - f[i-1] < mn:
        print("-1")
        break
else:
    surface = 0
    sizes = [-1] * n
    for i in range(n):
        size = mx
        
        #check ahead
        if i < n-1:
            size = min(size, 2*(f[i+1]-f[i]-(mn/2)))
        #check behind
        if i > 0:
            size = min(size, 2*(f[i]-f[i-1]-(sizes[i-1]/2)))

        sizes[i] = size

    print(int(sum(sizes)))