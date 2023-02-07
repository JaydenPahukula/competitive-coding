


s = ""
n = 1
product = 1
target = 1
while 1:
    s += str(n)
    if len(s) >= target:
        product *= int(s[target-1])
        if target == 1000000:
            break
        target *= 10
    n += 1
print(product)

