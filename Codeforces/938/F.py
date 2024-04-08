import sys
input=sys.stdin.readline

out = []
for _ in range(int(input())):
    a,b,c,d = map(int, input().split())
    wins = a+b+c+d//2
    p = a%2 + b%2 + c%2
    if min(a,b,c) > 0 and p >= 2:
        wins -= 2
        if not a%2: a-=1; wins -= 1
        if not b%2: b-=1; wins -= 1
        if not c%2: c-=1; wins -= 1
    else:
        wins -= p
    wins -= a//2 + b//2 + c//2
    out.append(wins)

print("\n".join(map(str, out)))
