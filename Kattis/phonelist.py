for _ in range(int(input())):
 l=sorted([input()for _ in range(int(input()))])
 for i in range(len(l)-1):
  if l[i+1].startswith(l[i]):
   print("NO")
   break
 else:
  print("YES")