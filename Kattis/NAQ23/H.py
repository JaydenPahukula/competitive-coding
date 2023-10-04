from functools import reduce

n,k,p = map(int, input().split())
output = []

def factors(n): return list(set((x, n//x) for x in reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
for a, b in factors(n):
    if a<=k and b<=p: output.append(a)

print(len(output))
print("\n".join(map(str, sorted(output))))