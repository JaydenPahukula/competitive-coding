n, g, p0, p1, p2 = map(float, input().split())

def P(gen):
    if gen == 0: return g
    p = P(gen-1)
    return (p*p*p2) + (2*p*(1-p)*p1) + ((1-p)*(1-p)*p0)

print(P(n))