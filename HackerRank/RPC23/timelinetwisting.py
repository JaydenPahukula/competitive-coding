N, C = map(int, input().split())
dur = list(map(int, input().split()))
d = {}
for _ in range(C):
    x, y, z = map(int, input().split())
    if z == 2: x,y=y,x
    if x in d: d[x].append(y)
    else: d[x] = [y]

mem = {}
def minTime(x):
    if x not in d: return dur[x]
    if x not in mem: mem[x] = dur[x]+max([minTime(y) for y in d[x]])
    return mem[x]

print(max([minTime(base) for base in range(N)]))