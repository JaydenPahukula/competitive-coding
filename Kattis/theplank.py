def f(t,c):
 if t<c:return 0
 if t==c:return 1
 return sum([f(t,c+d)for d in(1,2,3)])
print(f(int(input()),0))