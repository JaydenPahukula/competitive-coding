from collections import deque

T,X = map(int, input().split())
for _ in range(T):
    n = int(input())
    adj = [[]]
    count = 0
    green = [True]
    for i,x in enumerate(map(int, input().split())):
        adj[x-1].append(i+1)
        adj.append([])
    
    q = deque([(0,0,0,)])
    final = 0
    while q:
        curr,ifGreen,ifRed = q.popleft()
        print(curr, ifGreen, ifRed)

        final = max(0, max(ifGreen, ifRed))

        for neighbor in adj[curr]:
            q.append((neighbor,max(ifGreen,ifRed+1),max(ifGreen,ifRed)))
    
    print("    ", final)

        




        