from math import ceil
m,p,n = map(int,input().split())
curr = 0
numEpisodes = 0
for _ in range(n):
    w = int(input())
    if (w >= m+curr): numEpisodes += 1
    curr = ceil((m+curr-w)*p/100)
print(numEpisodes)