n = int(input())
last = ""
count = 0
for c in input():
    if c != last:
        count += 1
        last = c
print(count)