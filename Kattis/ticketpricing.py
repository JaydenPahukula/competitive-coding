R,M=range,map;N,W=M(int,input().split());d=[{0:(0,0)}]+[{}for _ in R(W+1)]
for w in R(W+1):
 k,*I=M(int,input().split())
 for p,a in zip(I[:k],I[k:]):
  for t in d[w]:
   r,f=d[w][t];s=min(N-t,a);t+=s;r+=p*s;w+=1
   if f==0:f=-p
   if t not in d[w]or r>d[w][t][0]:d[w][t]=r,f
a,b=max(d[W].values());print(a);print(-b)

# N,W=map(int,input().split())
# def R(week):
#  if week>0:
#   d=R(week-1);new={};k,*i=map(int,input().split())
#   for p,n in zip(i[:k],i[k:]):
#    for t in d:
#     r,f=d[t];s=min(N-t,n);r+=p*s;t+=s
#     if t not in new or r>new[t][0]:new[t]=r,f
#   return new
#  else:k,*i=map(int, input().split());return{s:(s*p,-p)for p,s in zip(i[:k],i[k:])}
# a,b=max(R(W).values());print(a);print(-b)