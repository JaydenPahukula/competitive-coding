from queue import PriorityQueue

def getDistance(a, b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**(1/2)

N = int(input())
for _ in range(N):
    M = int(input())

    islands = []
    for i in range(M):
        x, y = map(float, input().split())
        islands.append((x, y))

    totalDistance = 0
    connected = set()
    q = PriorityQueue()
    q.put((0, islands[0]))
    while len(connected) < M:
        distance, coords = q.get()

        if coords in connected: continue
        connected.add(coords)

        totalDistance += distance

        for destinationCoords in islands:
            if destinationCoords not in connected:
                q.put((getDistance(coords, destinationCoords), destinationCoords))

    print(totalDistance)






# N = int(input())
# for _ in range(N):
#     M = int(input())  
#     islands = []
#     connections = []
#     for i in range(M):
#         x, y = map(float, input().split())
#         islands.append((x, y, i))
#         connections.append(i)
    
#     def union(a:int, b:int):
#         finda = find(a)
#         findb = find(b)
#         if finda != findb:
#             connections[finda] = findb
#         return
    
#     def find(num:int):
#         if connections[num] == num:
#             return num
#         head = find(connections[num])
#         connections[num] = head
#         return head

#     bridges = []
#     for x1, y1, i in islands[:-1]:
#         for x2, y2, j in islands[i+1:]:
#             bridges.append((((x2-x1)**2+(y2-y1)**2)**(1/2), i, j))
#     bridges.sort()

#     totalDistance = 0
#     for distance, a, b in bridges:
#         if find(a) != find(b):
#             union(a, b)
#             totalDistance += distance

#     print(totalDistance)