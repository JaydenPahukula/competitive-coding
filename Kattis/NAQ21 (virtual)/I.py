dependOR = {}
dependAND = []
need = set()

def update(new:str):
    if new in dependOR:
        need.add(dependOR[new])
        dependOR.pop(new)
        update(dependOR[new])
    for s, n in dependAND:
        if new in s:
            s.remove(new)
            if len(s) == 0:
                need.add(n)
                update(n)
    return

for _ in range(int(input())):
    inp = input().split()
    if inp[0] == "if":
        dependant = inp[-1]
        if inp[2] == "or":
            for i in range(1, len(inp)-2, 2):
                if inp[i] in need:
                    need.add(dependant)
                    update(dependant)
                    break
                else:
                    dependOR[inp[i]] = dependant
        else:
            s = set([inp[i] for i in range(1,len(inp)-2,2) if inp[i] not in need])
            if len(s) == 0:
                need.add(dependant)
                update(dependant)
            else:
                dependAND.append((s, dependant))
    else:
        need.add(inp[0])
        update(inp[0])

print(len(need))