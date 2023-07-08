import heapq

N, K = map(int, input().split())
toSkip = {""}
q = []
for _ in range(N):
    inp = input().split()
    if inp[0] == "1":
        x, t, m, s = inp
        heapq.heappush(q, ((int(t)*K)-int(s), m))
    elif inp[0] == "2":
        x, t = inp
        name = ""
        if len(q) > 0:
            priority, name = heapq.heappop(q)
            while len(q) > 0 and name in toSkip:
                priority, name = heapq.heappop(q)
        if name == "":
            print("doctor takes a break")
        else:
            print(name)
    else:
        x, t, m = inp
        toSkip.add(m)