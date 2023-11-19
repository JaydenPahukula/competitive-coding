
import bisect

n=int(input())
ss=[]
es=[]
for _ in range(n):
    m,*a=map(int,input().split())
    l=a[0::2]
    r=a[1::2]
    ss.extend(l)
    es.extend(r)
ss.sort()
es.sort()
mx=0
ct=0
for i in range(0,86400):
    a=bisect.bisect_right(ss,i)
    b=bisect.bisect_left(es,i)
    v=a-b
    if v==mx:ct+=1
    elif v>mx:
        mx=v
        ct=1
    # print(i,a-b)
print(mx)
print(ct)

    


