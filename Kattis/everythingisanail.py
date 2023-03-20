n = int(input())
s = [0 for _ in range(12)]
for _ in range(n):
    task = int(input())
    if task == 0:
        s[0] += 1
        s[3] = max(s[3], s[1]) + 1
        s[6] = max(s[6], s[2]) + 1
        s[9] = max(s[9], s[4], s[8]) + 1
    elif task == 1:
        s[1] += 1
        s[4] = max(s[4], s[2]) + 1
        s[7] = max(s[7], s[0]) + 1
        s[10] = max(s[10], s[5], s[6]) + 1
    else:
        s[2] += 1
        s[5] = max(s[5], s[0]) + 1
        s[8] = max(s[8], s[1]) + 1
        s[11] = max(s[11], s[3], s[7]) + 1

print(max(s))
