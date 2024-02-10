import heapq

n,m = map(int, input().split())
a = [-int(x) for x in input().split()]
heapq.heapify(a)
for _ in range(m):
    heapq.heappush(a, heapq.heappop(a)/2)
print(sum([-int(x) for x in a]))
