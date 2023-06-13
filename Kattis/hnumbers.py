N = 1000002
final = [0 for _ in range(N)]
composites = set()
for h1 in range(5, N, 4):
    for h2 in range(h1, N, 4):
        h3 = h1 * h2
        if h3 >= N: break
        composites.add(h3)
        if h1 in composites or h2 in composites:
            final[h3] = 0
        else:
            final[h3] = 1

total = 0
for i in range(N):
    total += final[i]
    final[i] = total

while 1:
    n = int(input())
    if not n: break
    print(n, final[n])

