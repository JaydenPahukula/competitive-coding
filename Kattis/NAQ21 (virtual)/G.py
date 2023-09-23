c, n = map(int, input().split())
a = list(map(int, input().split()))
pairsina = []
pairsnot = []
if a[0] != 1: pairsnot.append((1,a[0]-1))
start = a[0]
for i in range(1,n):
    if a[i]-a[i-1] != 1:
        pairsina.append((start,a[i-1]))
        pairsnot.append((a[i-1]+1,a[i]-1))
        start = a[i]
pairsina.append((start,a[-1]))
if a[-1] != c: pairsnot.append((a[-1]+1,c))
if len(pairsina) > 1:
    print("Errors:",", ".join([(str(a) if a==b else f"{a}-{b}") for a,b in pairsina[:-1]]),"and",[(str(a) if a==b else f"{a}-{b}") for a,b in pairsina[-1:]][0])
else:
    print("Errors:",[(str(a) if a==b else f"{a}-{b}") for a,b in pairsina][0])
if len(pairsnot) > 1:
    print("Correct:",", ".join([(str(a) if a==b else f"{a}-{b}") for a,b in pairsnot[:-1]]),"and",[(str(a) if a==b else f"{a}-{b}") for a,b in pairsnot[-1:]][0])
else:
    print("Correct:",[(str(a) if a==b else f"{a}-{b}") for a,b in pairsnot][0])