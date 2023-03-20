s = input()
n = len(s)
solutions = []
for k in range(1, n+1):
    awins = 0
    bwins = 0
    ascore = 0
    bscore = 0
    for c in s:
        if c == "A": ascore += 1
        else:        bscore += 1
        if ascore >= k:
            ascore = 0
            bscore = 0
            awins += 1
        elif bscore >= k:
            ascore = 0
            bscore = 0
            bwins += 1
    if awins > bwins: solutions.append(k)

print(len(solutions))
print(" ".join(map(str, solutions)))