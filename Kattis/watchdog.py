def check(s,H):
 for X in range(1,s):
  for Y in range(1,s):
   for x,y in H:
    if(x,y)==(X,Y)or((X-x)**2+(Y-y)**2)**(0.5)>min((X,Y,s-X,s-Y)):break
   else:return f"{X} {Y}"
 return"poodle"
for _ in range(int(input())):
 s,n=map(int,input().split())
 h=[tuple(map(int,input().split()))for _ in range(n)]
 print(check(s,h))


# import math

# def check(s, hatches):
#     for x in range(1, s):
#         for y in range(1, s):
#             limit = min([x, y, s-x, s-y])
#             for hatch in hatches:
#                 if hatch[0] == x and hatch[1] == y:
#                     break
#                 if math.sqrt((x-hatch[0])**2 + (y-hatch[1])**2) > limit:
#                     break
#             else:
#                 return (x, y)
#     return False


# for _ in range(int(input())):
#     s, h = map(int, input().split())
#     hatches = [tuple(map(int, input().split())) for _ in range(h)]
    
#     result = check(s, hatches)
#     if result:
#         print(result[0], result[1])
#     else:
#         print("poodle")