s=input();p=input();print(("No","Yes")[(s==p)or(p==s[:-1]and s[-1].isdigit())or(p==s[1:]and s[0].isdigit())or(s==p.swapcase())])



# s = input()
# p = input()
# if s==p or (s[:-1]==p and s[-1].isdigit()) or (s[1:]==p and s[0].isdigit()) or (s=="".join([c.upper() if c.islower() else c.lower() for c in p])):
#     print("Yes")
# else:
#     print("No")