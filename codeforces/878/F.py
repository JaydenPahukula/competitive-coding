import heapq

for _ in range(int(input())):
    n, m = map(int, input().split())
    r = int(input())
    raw = [tuple(map(int, input().split())) for _ in range(r)]
    mx = max([x[0] for x in raw])+n+m
    shots = [list() for _ in range(mx)]
    for t, d, coord in raw:
        shots[t-1].append((d, coord))
    
    q = [(0, 0)]

    for t in range(mx):
        print("t =", t)

        qlen = len(q)
        if qlen == 0:
            print("-1")
            break
        for _ in range(qlen):
            currx, curry = heapq._heappop_max(q)
            #print(currx, curry)

            if currx == n and curry == m:
                break
            
            canStay = True
            canUp = True
            canRight = True
            for d, coord in shots[t]:
                if d == 1:
                    if coord == curry:
                        canStay = False
                        canRight = False
                    if coord == curry+1:
                        canUp = False
                if d == 2:
                    if coord == currx:
                        canStay = False
                        canUp = False
                    if coord == currx+1:
                        canRight = False
            if canStay:
                heapq.heappush(q, (currx, curry))
            if canUp and curry < m-1:
                heapq.heappush(q, (currx, curry+1))
            if canRight and currx < n-1:
                heapq.heappush(q, (currx+1, curry))
        else:
            heapq._heapify_max(q)
            continue
        print(t)
        break
    else:
        print(-1)
    print()
    print()