while 1:
    n = int(input())
    if n == -1: break

    rings = [tuple(map(float, input().split())) for _ in range(n)]
    a = [[i, 1] for i in range(n)]

    for i, ring1 in enumerate(rings):
        x1, y1, r1 = ring1
        for j, ring2 in enumerate(rings):
            if j <= i: continue
            x2, y2, r2 = ring2
            if (x1-x2)**2 + (y1-y2)**2 < (r1+r2)**2 and (x1-x2)**2 + (y1-y2)**2 >= abs(r1-r2):
                a[i][0] = j
                a[j][1] += a[i][1]
    
    solution = max(a, key=lambda x:x[1])[1]
    s = 's'
    if solution == 1: s = ''
    print(f"The largest component contains {solution} ring{s}.")
