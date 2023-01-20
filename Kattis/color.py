
S, C, K = map(int, input().split(' '))
D = list(map(int, input().split(' ')))
D.sort()

washingMachine = D[0]
capacity = 1
count = 1
for sock in D[1:]:
    if sock <= washingMachine+K and capacity < C:
        capacity += 1
    else:
        washingMachine = sock
        capacity = 1
        count += 1

print(count)
