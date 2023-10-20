import itertools as i;n=input()
for x in map("".join,sorted(i.permutations(n))):
 if x>n:print(x);break
else:print(0)