N,S=map(int,input().split())
a,c,o=sorted([tuple([(int(y),x)for x,y in [input().split()]][0]) for _ in range(N)])[::-1],0,[]
for n,m in a:
 if c+n==S:
  print(len(o)+1,"\n"+"\n".join(o+[m]))
  break
 if c+n<S:
  o.append(m)
  c+=int(n)
else:print(0)