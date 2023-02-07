


total = -1
for n in range(1000000):
    s = str(n)
    x = 0
    for c in s:
        x += int(c)**5
    if n == x:
        total += n
print(total)