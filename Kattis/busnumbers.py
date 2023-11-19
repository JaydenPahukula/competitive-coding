n = int(input())
a = sorted(map(int,input().split()))

i = 0
out = []
while i < n:
    j = i
    while j < n-1 and a[j+1]-a[i] == j-i+1: j += 1

    if j == i:
        out.append(str(a[i]))
    elif j == i+1:
        out.append(str(a[i]))
        out.append(str(a[j]))
    else:
        out.append(f"{a[i]}-{a[j]}")

    i = j+1
print(" ".join(out))