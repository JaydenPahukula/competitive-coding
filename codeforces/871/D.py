from collections import deque

for _ in range(int(input())):
    start, target = map(int, input().split())
    if target > start:
        print("NO")
        continue
    q = deque()
    visited = {start}
    q.append(start)
    while q:
        curr = q.popleft()
        if curr == target:
            print("YES")
            break
        if curr % 3 != 0:
            continue
        else:
            q.append(2*curr//3)
            q.append(curr//3)
    else:
        print("NO")
