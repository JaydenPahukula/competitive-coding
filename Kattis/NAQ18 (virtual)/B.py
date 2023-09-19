def gcd(a:int, b:int):
    while(b):
       a, b = b, a % b
    return abs(a)

p, q, s = map(int, input().split())
if p*q//gcd(p,q) <= s: print("yes")
else: print("no")