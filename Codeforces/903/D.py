
def primeFactors(n:int):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

for _ in range(int(input())):
    n = int(input())
    l = [primeFactors(int(x)) for x in input().split()]
    d = {}
    for factorlist in l:
        for factor in factorlist:
            if factor in d: d[factor] += 1
            else: d[factor] = 1
    for count in d.values():
        if count%n != 0:
            print("NO")
            break
    else:
        print("YES")
