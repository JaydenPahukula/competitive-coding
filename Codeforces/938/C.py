import sys
input=sys.stdin.readline

out = []
for _ in range(int(input())):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))

    start = 0
    attack = -(k//-2)
    while start < n:
        if a[start] <= attack:
            attack -= a[start]
            start += 1
        else:
            a[start] -= attack
            break
    end = n-1
    attack = k//2
    while end >= 0 and end >= start and attack >= a[end]:
        attack -= a[end]
        end -= 1

    out.append(start + n-1-end)

print("\n".join(map(str, out)))
