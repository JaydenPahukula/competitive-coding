n = int(input())
a = sorted([int(input()) for _ in range(n)])

count = 0
for x in a[::-1]:
    if count >= x:
        print(count)
        break
    count += 1
else:
    print(n)
