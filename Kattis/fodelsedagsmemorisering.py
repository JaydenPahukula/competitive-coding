n = int(input())
bdays = {}
for _ in range(n):
    name, priority, bday = input().split(' ')
    if bday in bdays:
        bdays[bday].append((name, priority))
    else:
        bdays[bday] = [(name, priority)]
print(len(bdays))
names = []
for bd in bdays.keys():
    bdays[bd].sort(key=lambda x:int(x[1]), reverse=True)
    names.append(bdays[bd][0][0])
for name in sorted(names):
    print(name)
