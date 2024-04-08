import sys
input=sys.stdin.readline

out = []
for _ in range(int(input())):
    n,c,d = map(int, input().split())
    a = {}
    for x in map(int, input().split()):
        if x not in a: a[x] = 1
        else: a[x] += 1

    def check():
        start = min(a)
        for y in range(n):
            for x in range(n):
                num = start + c*x + d*y
                if num not in a or a[num] <= 0: return False
                a[num] -= 1
        return True

    if check():
        out.append("YES")
    else:
        out.append("NO")

print("\n".join(map(str, out)))
