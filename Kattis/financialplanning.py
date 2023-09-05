n,M=map(int,input().split())
v,t,b,m,x=[tuple(map(int,input().split())) for _ in range(n)],10**11,0,0,0
while b<t:
 m=(t+b)//2
 if sum([max(p*m-c,0) for p,c in v])<M:b=m+1
 else:t,x=m,m
print(x)