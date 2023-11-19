n,m,q=map(int,input().split())
g=[([c=='Y' for c in input()],i+1) for i in range(n)]
for _ in range(q):
    a,b=input().split()
    a=int(a)
    b=b=='Y'
    g=[r for r in g if r[0][a-1]==b]

if len(g)==1:
    print('unique')
    print(g[0][1])
else:
    print('ambiguous')
    print(len(g))

