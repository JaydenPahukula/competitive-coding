m, n = map(int, input().split())
d = {}
for _ in range(m):
    word, val = input().split()
    d[word] = int(val)
for _ in range(n):
    score = 0
    line = input()
    while line != ".":
        for word in line.split():
            if word in d:
                score += d[word]
        line = input()
    print(score)