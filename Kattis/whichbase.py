for _ in "_"*int(input()):
 i,s=input().split()
 print(i,0 if "8" in s or "9" in s else int(s,8),int(s,10),int(s,16))