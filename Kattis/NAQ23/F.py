s = input()
c1 = 0
c2 = 0
for c in s:
    if c in {"a","e","i","o","u"}:
        c1 += 1
        c2 += 1
    if c == "y":
        c2 += 1
print(c1, c2)