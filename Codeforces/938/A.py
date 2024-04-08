import sys
input=sys.stdin.readline

out = []
for _ in range(int(input())):
    n,a,b = map(int, input().split())
    if a*2 < b:
        out.append(n*a)
    else:
        out.append(n//2*b + n%2*a)

print("\n".join(map(str, out)))
