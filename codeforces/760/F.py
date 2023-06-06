def f(n:int):
    return (int('1'+bin(n)[:1:-1], 2), int(bin(n)[:1:-1], 2))

start, end = map(int, input().split())
q = [start]
visited = {start}
while q:
    curr, *q = q
    if curr == end:
        print("YES")
        break
    if curr > 10**30:
        print("NO")
        break
    for x in f(curr):
        if x not in visited:
            visited.add(x)
            q.append(x)
else:
    print("NO")