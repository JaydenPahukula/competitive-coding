for _ in range(int(input())):
    v, e = map(int, input().split())
    numConnections = [0 for _ in range(v)]
    for _ in range(e):
        a, b = map(int, input().split())
        numConnections[a-1] += 1
        numConnections[b-1] += 1
    s = list(set(numConnections))
    s.remove(1)
    if len(s) < 2:
        print(f"{s[0]} {s[0]-1}")
    elif numConnections.count(s[0]) == 1:
        print(f"{s[0]} {s[1]-1}")
    else:
        print(f"{s[1]} {s[0]-1}")