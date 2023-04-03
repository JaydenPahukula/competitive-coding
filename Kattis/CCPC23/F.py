n = int(input())
vault = [[int(input()), 0] for _ in range(n)]
vault.sort()

for i in range(n-1):
    num = vault[i][0]
    numMultiples = 0
    for j in range(i+1, n):
        if num % vault[j][0] == 0:
            numMultiples += 1
    vault[i][1] = numMultiples

vault.sort(key = lambda x: (-x[1], x[0]))

print(vault)