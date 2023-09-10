p,m=input().split()
for c in m:
 if c==p[0]:
  p=p[1:]
 elif c in p:
  print("FAIL")
  break
 if not p:
  print("PASS")
  break
else:
 print("FAIL")