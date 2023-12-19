from collections import deque

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    children = [[] for _ in range(n)]
    for i in range(n-1):
        children[a[i]-1].append(i+1)
    
    print(children)
    q = deque([0])
    score = 0
    while q:
        l = len(q)
        for _ in range(l):
            curr = q.popleft()
            for child in children[curr]:
                q.append(child)
        score += len(q)//2
    
    print(score)