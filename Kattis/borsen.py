from collections import deque

n = int(input())
fee = float(input())
a = [float(input()) for _ in range(n)]
q = deque({(100.0, True)})

for i in range(n):
    price = a[i]
    
    qlen = len(q)
    for _ in range(qlen):
        val, liquid = q.popleft()

        if liquid: #buy
            q.append(((val-fee)/price, False))
        else: #sell
            q.append(((val*price)-fee, True))
        
        q.append((val, liquid)) #do nothing

mx = 0
while q:
    val, liquid = q.pop()
    if liquid and val > mx:
        mx = val
print(mx)