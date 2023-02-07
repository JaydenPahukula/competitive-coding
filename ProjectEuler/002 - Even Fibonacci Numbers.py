a = 1
b = 1
sum = 0
while 1:
    a += b
    if a > 4000000:
        break
    if a % 2 == 0:
        sum += a
    b += a
    if b > 4000000:
        break
    if b % 2 == 0:
        sum += b
print(sum)
