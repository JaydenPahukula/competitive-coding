
numPlanets = int(input())
whereFrom = {}
planetCounts = {}
for _ in range(numPlanets):
    inp = input().split()
    planetCounts[inp[0]] = 0
    for species in inp[2:]:
        whereFrom[species] = inp[0]

v = int(input())
for _ in range(v):
    numVisitors, species = input().split()
    planetCounts[whereFrom[species]] += int(numVisitors)

for p in sorted(planetCounts.keys()):
    print(p, planetCounts[p])