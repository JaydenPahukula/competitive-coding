count = 0
for x in input().split(';'):
    count += 1
    if '-' in x:
        a, b = map(int, x.split('-'))
        count += b-a
print(count)