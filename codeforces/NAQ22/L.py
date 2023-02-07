t, s = map(int, input().split(" "))
taxi = 1 + 2 * t * (1 + t)

spidey_num = 0
increment = 1

for i in range(1, s+1):
    spidey_num += i + i//3

spidey_num= 1 + 4 * spidey_num

d = 0
gt175 = False
if spidey_num <= taxi and taxi <= 2 * spidey_num:

    index = 0
    while True:
        prev_d = -1
        if t==index:
            gt175=True
        for i in range(-1 * index, index + 1):
            if abs(i) + abs(t - index) - abs(i)//2 > s:
                d += 1
                prev_d=1
        if prev_d == -1:
            break
        index += 1
elif taxi >= 2*spidey_num:
    gt175 = True

taxi -= 4 * d

divisor = 1
lesser = spidey_num if spidey_num < taxi else taxi
for i in range(1, lesser+1):
    if spidey_num % i == 0 and taxi % i == 0:
        divisor = i

spidey_num /= divisor
taxi /= divisor

spidey_num = int(spidey_num)
taxi = int(taxi)


if gt175:
    print(1)
elif spidey_num == 1:
    print(taxi)
else:
    print(f"{taxi}/{spidey_num}")