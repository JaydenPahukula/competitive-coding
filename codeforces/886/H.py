for _ in range(int(input())):
    n, m = map(int, input().split())
    placed = {}
    floating = {}
    a, b, d = map(int, input().split())
    placed[b] = 0
    placed[a] = d
    for i in range(m-1):
        a, b, d = map(int, input().split())
        if b not in placed and a not in placed:
            floating[a] = (b, d)
            floating[b] = (a, d)
        elif b in placed:
            if a in placed:
                if placed[a]-placed[b] != d: break
            elif a in floating:
                placed[a] = placed[b] + d
                placed[floating[a][0]] = placed[a] - placed[floating[a][1]]
                floating.pop(a)
                floating.pop(b)
            else:
                placed[a] = placed[b] + d
        elif a in placed:
            if b in floating:
                placed[b] = placed[a] - d
                placed[floating[b][0]] = placed[b] - placed[floating[b][1]]
                floating.pop(a)
                floating.pop(b)
            else:
                placed[b] = placed[a] - d
    else:
        print("YES")
        continue
    print("NO")