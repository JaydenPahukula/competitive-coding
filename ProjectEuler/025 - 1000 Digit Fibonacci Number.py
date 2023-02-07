

numDigits = 1000

i = 1
a = 0
b = 1
while 1:
    a += b
    i += 1
    if len(str(a)) == numDigits:
        break
    b += a
    i += 1
    if len(str(b)) == numDigits:
        break
print(i)

