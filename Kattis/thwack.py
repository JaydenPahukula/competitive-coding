n=int(input())
s=input()

cache={}
def solve(s):
    if s in cache:return cache[s]
    pos=set()
    for i in range(len(s)-1):
        if s[i]!=s[i+1]:
            l1=s[:i]+s[i+1]
            l2=s[:i]
            r1=s[i+2:]
            r2=s[i]+s[i+2:]
            # print(s)
            # print(l1,r1)
            # print(l2,r2)
            g1=solve(l1)^solve(r1)
            g2=solve(l2)^solve(r2)
            pos.add(g1)
            pos.add(g2)
    mex=0
    while mex in pos:mex+=1
    cache[s]=mex
    return mex


og=s
parts=s.split('.')
prev=0
good=[]
rest=0
for s in parts:rest^=solve(s)
for s in parts:
    otr=rest^solve(s)
    for i in range(len(s)-1):
        if s[i]!=s[i+1]:
            l1=s[:i]+s[i+1]
            l2=s[:i]
            r1=s[i+2:]
            r2=s[i]+s[i+2:]
            g1=solve(l1)^solve(r1)^otr
            g2=solve(l2)^solve(r2)^otr
            if g1==0:good.append((prev+i,prev+i+1))
            if g2==0:good.append((prev+i+1,prev+i))
    prev+=len(s)+1
good=[(y+1,x+1) for x,y in good]
good.sort()
print(len(good))
for x,y in good:
    print(x,y)
# print(cache)



