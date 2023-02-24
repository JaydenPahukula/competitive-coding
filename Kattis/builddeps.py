n = int(input())
files = {}
inverse = {}
zeroes = set()
for _ in range(n):
    inp = input().split()
    files[inp[0][:-1]] = inp[1:]
    if inp[1:] == []:
        zeroes.add(inp[0][:-1])
    inverse[inp[0][:-1]] = []
changedFile = input()

#make an inverse list of dependancies
for file in files.keys():
    for dependant in files[file]:
        inverse[dependant].append(file)

#remove everything not dependant on changedFile
while len(zeroes) > 0:
    curr = zeroes.pop()
    if curr == changedFile: continue
    for dependant in inverse[curr]:
        files[dependant].remove(curr)
        if len(files[dependant]) == 0:
            zeroes.add(dependant)

#go through the rest of the tree
q = {changedFile}
while len(q) > 0:
    curr = q.pop()
    print(curr)
    for dependant in inverse[curr]:
        files[dependant].remove(curr)
        if len(files[dependant]) == 0:
            q.add(dependant)

