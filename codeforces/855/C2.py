import heapq

for _ in range(int(input())):
    q = []
    n = int(input())
    score = 0
    for x in map(int, input().split()):
        if x == 0:
            if len(q) > 0:
                score += -heapq.heappop(q)
        else:
            heapq.heappush(q, -x)
    print(score)