from math import log2, ceil

n, k = map(int, input().split())

for x in range(1, n+1):
    if x >= ceil(log2(x+1))*k:
        print("Good to go!")
        break
else:
    print("Tweak the bounds!")