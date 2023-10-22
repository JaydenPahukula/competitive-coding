n = int(input())
d = {}
for _ in range(n):
    pred, prey = input().split(" <- ")
    for x in prey.split(", "):
        if x in d: d[x].append(pred)
        else: d[x] = [pred]

mem = {}
def numPred(s):
    if s not in d: return 1
    if s not in mem: mem[s] = 1+max([numPred(x) for x in d[s]])
    return mem[s]

print(max([numPred(base) for base in d]))