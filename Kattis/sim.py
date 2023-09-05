for _ in range(int(input())):
 l,i=[[]],0
 for c in input():
  if c=="<":
   while not l[i] and i<len(l)-1:i+=1
   if not l[i] and len(l)-2-i:continue
   l[i].pop()
  elif c=="[":i,x=len(l),l.append([])
  elif c=="]":i=0
  else:l[i].append(c)
 print("".join(sum(l[::-1],[])))