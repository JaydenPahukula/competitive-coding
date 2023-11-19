from collections import deque
import heapq

p,n=map(int,input().split())
left=[deque([]) for _ in range(p)]
right=[deque([]) for _ in range(p)]
lefta=[-1000]*p
leftb=[-1000]*p
righta=[-1000]*p
rightb=[-1000]*p
finish=[0]*n
events=[]

for car in range(n):
    t,f,s=input().split()
    t=int(t)
    f=int(f)
    events.append((t,10,s,('queue',f,car)))

heapq.heapify(events)

while len(events):
    t,_,s,op=heapq.heappop(events)
    use=left if s=='L' else right
    usea=lefta if s=='L' else righta
    useb=leftb if s=='L' else rightb
    if op[0]=='queue':
        _,f,car=op
        best=(50000,0)
        # assume state is completely updated!
        for i in range(p):
            if usea[i]<=t:
                if useb[i]<=t:
                    useb[i]=t+f
                    finish[car]=t+f
                else:
                    usea[i]=t+f
                    finish[car]=t+f
                heapq.heappush(events,(t+f,0,s,('finish',)))
                break
            best=min(best,(len(use[i]),i))
        else:
            use[best[1]].append((car,f))

    for i in range(p):
        aop = usea[i]<=t
        bop = useb[i]<=t
        if not aop:continue
        if bop:
            if len(use[i]):
                car,f=use[i].popleft()
                useb[i]=t+f
                finish[car]=t+f
                heapq.heappush(events,(t+f,0,s,('finish',)))
            if len(use[i]):
                car,f=use[i].popleft()
                usea[i]=t+f
                finish[car]=t+f
                heapq.heappush(events,(t+f,0,s,('finish',)))
        else:
            if len(use[i]):
                car,f=use[i].popleft()
                usea[i]=t+f
                finish[car]=t+f
                heapq.heappush(events,(t+f,0,s,('finish',)))

for v in finish:print(v)
