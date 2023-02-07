length = 1001

sum = 1
i = 1
for x in range(int((length-1)/2)):
    for y in range(4):
        i += 2+(2*x)
        print(i)
        sum += i
print(sum)