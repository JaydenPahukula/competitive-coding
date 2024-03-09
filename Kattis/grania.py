from math import gcd

def factors(n):
    return [item for pair in [(x,n//x) if x!=n//x else (x,) for x in range(1,int(n**0.5)+1) if n%x==0] for item in pair]

n = int(input())
a = [int(input()) for _ in range(n)]

d = [a[i]-a[i-1] for i in range(1,n)]

g = gcd(*d)

print("\n".join(str(x) for x in factors(g) if x != 1))
