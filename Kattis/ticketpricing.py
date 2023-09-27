n,w=map(int,input().split())
dp=[{0:(0, 0)}]+[{}for _ in range(w+1)]
for week in range(w+1):
 I=list(map(int, input().split()))
 for i in range(I[0]):
  p,d=I[1+i],I[I[0]+1+i]
  for t in dp[week]:
   r,f=dp[week][t]
   if f==0:f=-p
   s=min(n-t,d)
   t+=s
   if t not in dp[week+1]or r+p*s>dp[week+1][t][0]:dp[week+1][t]=(r+p*s,f)
a,b=max(dp[-1].values())
print(a)
print(-b)