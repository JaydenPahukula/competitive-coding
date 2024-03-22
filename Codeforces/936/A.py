import sys
input=sys.stdin.readline

out = []
for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    middle = i = (n-1)//2
    count = 0
    while i < n and a[i] == a[middle]:
        count += 1
        i += 1
    out.append(count)
print("\n".join(map(str, out)))
