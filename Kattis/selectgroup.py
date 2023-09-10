import sys
g,i,l = {},0,[]
def f():
 global i
 i+=1
 if l[i]=="union":o=f().union(f())
 elif l[i]=="intersection":o=f().intersection(f())
 elif l[i]=="difference":o=f().difference(f())
 else:o=g[l[i]]
 return o
for line in sys.stdin:
 i,l = -1,line.split()
 if l[0] == "group":g[l[1]] = set(l[3:])
 else:print(" ".join(sorted(f())))