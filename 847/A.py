PI = "3141592653589793238462643383279"
numTestCases = int(input())
for _ in range(numTestCases):
    score = 0
    for i, c in enumerate(input()):
        if c != PI[i]:
            break
        score += 1
    print(score)