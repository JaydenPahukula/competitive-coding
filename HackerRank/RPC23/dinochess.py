m, n = map(int, input().split())
on = True
count = 0
i = 0
while i < n:
    i += 1
    if on: count += 1
    if i%m == 0: on = not on

print(count*count)