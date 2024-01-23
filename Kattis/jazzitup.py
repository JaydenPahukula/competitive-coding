from math import sqrt

def factors(n):
    return [item for pair in [(x,n//x) if x!=n//x else (x,) for x in range(1,int(n**0.5)+1) if n%x==0] for item in pair]

def isSquare(n):
    return abs(0.5-(n**0.5+0.5)%1) > 0.001

n = int(input())
for m in range(2,n):
    for factor in factors(n*m):
        if factor == 1: continue
        print(factor)
        if isSquare(factor):
            break
    else:
        print(m)
        break