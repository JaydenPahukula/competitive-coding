I=input
for C in","*int(I()):
 a,r=[0]*3,0
 for c in I():
  if"R"==c:r=2-r
  else:a[r]+=1
 b=int(I())-a[2];print((f"[{C.join(I()[1:-1].split(C)[a[0]:b][::1-r])}]","error")[a[0]>b])

# for _ in range(int(input())):
#     instructions = input()
#     n = int(input())
#     l = list(input()[1:-1].split(","))
#     a,b,r = 0,0,0
#     for c in instructions:
#         if c == "R":r=1-r
#         elif r: b+=1
#         else: a+=1
#     if n-b < a: print("error")
#     else: print(f"[{','.join(l[a:n-b][::-1 if r else 1])}]")