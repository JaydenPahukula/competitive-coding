I=99;N=int(input());A=[(x,y)for y in range(N)for x,c in enumerate(input())if'.'!=c];l=len(A);o=0
for i in range(l):
 a,b=A[i]
 for j in range(i+1,l):
  c,d=A[j]
  if a!=c:M=(b-d)/(a-c);B=b-M*a
  else:M=I;B=a
  for e,f in A[j+1:]:
   if M!=I and .01>abs(f-M*e-B)or M==I and abs(e-B)<.01:o+=1
print(o)


# INFINITY = 143798567.13491495
# ERROR = 0.0001
# n = int(input())
# grid = [[c!="." for c in input()] for _ in range(n)]
# total = 0
# points = []
# for y in range(n):
#     for x in range(n):
#         if grid[y][x]: points.append((x,y))
# for i in range(len(points)):
#     x1,y1 = points[i]
#     for j in range(i+1,len(points)):
#         x2,y2 = points[j]
#         m = (y1-y2)/(x1-x2) if x1 != x2 else INFINITY
#         b = y1-m*x1 if x1 != x2 else x1
#         for k in range(j+1,len(points)):
#             x3,y3 = points[k]
#             if m!=INFINITY and abs(y3-m*x3-b)<ERROR or m==INFINITY and abs(x3-b)<ERROR:
#                 total += 1
# print(total)