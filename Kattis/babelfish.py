import sys
lines = sys.stdin.readlines()
i,d = 0,{}
while lines[i] != "\n":
    a,b = lines[i].strip().split()
    d[b] = a
    i += 1
while i+1<len(lines):
    i += 1
    c = lines[i].strip()
    if c in d: print(d[c])
    else: print("eh")
