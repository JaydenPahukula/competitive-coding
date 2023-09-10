n,T=[input() for _ in range(int(input()))],"ThoreHusfeldt"
if n[0]==T:print("Thore is awesome")
else:
 n,o=n[:n.index(T)],1
 for m in n:
  if m.startswith(T[:-1]):
   print("Thore sucks")
   break
 else:
  for m in n:
   while m.startswith(T[:o]):o+=1
  print(T[:o])