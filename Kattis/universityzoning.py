h, w, f, s, g = map(int, input().split())
zones = [[] for _ in range(f)]
for i in range(f):
    inp = list(map(int, input().split()))
    zones[i] = [(inp[x*2+1]-1, inp[x*2+2]-1) for x in range(inp[0])]
students = [[] for _ in range(f)]
for _ in range(s):
    y, x, num, zone = map(int, input().split())
    students[zone-1].append((num, y-1, x-1))

t = list(map(int, input().split()))

steps = 0

for z in range(f):
    students[z].sort()
    zones[z].sort()
    stepsNeeded = [abs(zones[z][student][0]-students[z][student][1])+abs(zones[z][student][1]-students[z][student][2]) for student in range(len(students[z]))]
    steps += sum(sorted(stepsNeeded)[:t[zone]])
print(steps)