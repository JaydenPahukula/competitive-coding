
numTestCases = int(input())

for case in range(numTestCases):
    n = int(input())
    a = [int(item) for item in input().split(' ')]
    i = 0
    while a[i] == 0 and i < n-1:
        i += 1
    moves = sum([1 if x == 0 else 0 for x in a[i:-1]]) + sum(a[:-1])
    
    print(moves)