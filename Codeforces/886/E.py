from math import sqrt

def q(m, n, c):
    return int((-m + sqrt(m*m + 16*n*c)) / (8*n))

for _ in range(int(input())):
    n, c = map(int, input().split())
    l = list(map(int, input().split()))
    c -= sum([s*s for s in l])
    m = 4*sum(l)
    print(q(m, n, c))
