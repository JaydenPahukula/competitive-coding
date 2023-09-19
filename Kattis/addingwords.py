import sys
d,p={},{"-":-1,"+":1,"calc":1}
for r in sys.stdin.readlines():
 l = r.split()
 if l[0]=="def":
  if l[1]in d:d.pop(d[l[1]])
  d[l[1]],d[l[2]]=l[2],l[1]
 elif l[0]=="calc":
  o=0
  for i in range(0,len(l)-1,2):
   if l[i+1]not in d:o=9**99
   else:o+=int(d[l[i+1]])*p[l[i]]
  print(" ".join(l[1:]),end=" ")
  if str(o)in d:print(d[str(o)])
  else:print("unknown")
 else:d={}