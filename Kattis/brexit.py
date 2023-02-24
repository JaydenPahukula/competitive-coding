C, P, X, L = map(int, input().split())
tradePartners = [[] for _ in range(C)]
initNumTradePartners = [0 for _ in range(C)]
for _ in range(P):
    A, B = map(int, input().split())
    tradePartners[A-1].append(B-1)
    initNumTradePartners[A-1] += 1
    tradePartners[B-1].append(A-1)
    initNumTradePartners[B-1] += 1

left = [False for _ in range(C)]
left[L-1] = True
numTradePartners = initNumTradePartners.copy()
def solve():
    if X == L:
        return "leave"
    q = [L-1]
    while q:
        curr = q.pop()
        for country in tradePartners[curr]:
            if left[country]: continue
            numTradePartners[country] -= 1
            if numTradePartners[country] <= initNumTradePartners[country]/2:
                if country == X-1:
                    return "leave"
                left[country] = True
                q.append(country)
    return "stay"

print(solve())



