from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
seta = defaultdict(lambda: 0)
setb = defaultdict(lambda: 0)
output = []
for i in range(n):
    seta[a[i]] += 1
    setb[b[i]] += 1
    output.append(str(b[i]))
    if seta == setb:
        output.append("#")
        seta.clear()
        setb.clear()
print(" ".join(output[:-1]))