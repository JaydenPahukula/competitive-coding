n = int(input())
intervals = sorted([tuple(map(int, input().split())) for _ in range(n)])
i = 0
count = 0
while i < n:
    temp = intervals[i][1]
    i += 1
    while i < n and intervals[i][0] <= temp:
        temp = min(temp, intervals[i][1])
        i += 1
    count += 1
print(count)