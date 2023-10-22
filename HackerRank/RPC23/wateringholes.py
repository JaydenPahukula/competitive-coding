n = int(input())
wateringholes = {}
seen = set()
for _ in range(n):
    name, num = input().split()
    if name in wateringholes: wateringholes.pop(name)
    if int(num) != 0:
        seen.add(int(num))
        wateringholes[name] = int(num)

inverse = {}
maxNum = 0
for name in wateringholes:
    num = wateringholes[name]
    if num in inverse: inverse[num].append(name)
    else: inverse[num] = [name]

for num in sorted(list(seen)):
    print(num, end=" ")
    if num in inverse:
        print(" ".join(sorted(inverse[num])))
    else:
        print("n/a")