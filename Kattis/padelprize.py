n, m = map(int, input().split())
medals = [-1 for _ in range(m)]
totalTime = [[0 for _ in range(n)] for _ in range(m)]

for i in range(m):
    winner, loser = map(int, input().split())
    for j in range(i):
        if medals[j] == loser: medals[j] = winner
    medals[i] = winner

    for medal, holder in enumerate(medals[:i+1]):
        totalTime[medal][holder] += 1

medalCounts = [0 for _ in range(n)]
for times in totalTime:
    winner = times.index(max(times))
    medalCounts[winner] += 1

print(" ".join(map(str, medalCounts)))