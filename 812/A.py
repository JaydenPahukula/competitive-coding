
numTestCases = int(input())

for case in range(numTestCases):
    n = int(input())
    x = [0]
    y = [0]
    for box in range(n):
        x1, y1 = map(int, input().split(' '))
        x.append(x1)
        y.append(y1)
    print(2*(abs(min(x))+max(x)) + 2*(abs(min(y))+max(y)))
