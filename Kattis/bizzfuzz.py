from math import gcd
a,b,c,d = map(int, input().split())
print(b//(c*d//gcd(c,d))-(a-1)//(c*d//gcd(c,d)))