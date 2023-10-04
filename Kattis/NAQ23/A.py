n,k,c = map(int, input().split())
isAdvancing = []
schoolcount = {}
for i in range(n):
    team,school = map(int, input().split())
    isAdvancing.append((team,False))
    if k == 0: continue
    if school not in schoolcount:
        schoolcount[school] = 1
    else: schoolcount[school] += 1
    if schoolcount[school] > c: continue
    isAdvancing[i] = (team, True)
    k -= 1
for i in range(n):
    if k == 0: break
    team, isA = isAdvancing[i]
    if not isA:
        isAdvancing[i] = (team,True)
        k -= 1
print("\n".join([str(team) for team, isA in isAdvancing if isA]))