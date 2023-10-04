n, lph = map(int, input().split())
l = lph*5
count = 0
problems = sorted([int(input()) for _ in range(n)])
for problem in problems:
    if l-problem < 0: break
    l-= problem
    count += 1
print(count)