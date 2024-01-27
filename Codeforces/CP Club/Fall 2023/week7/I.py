from math import log2
import sys
input = sys.stdin.readline

bits = [[99**9]*18 for _ in range(2*10**5+2)]
bits[0] = [0]*18
for i in range(1,2*10**5+2):
    xl = len(bits[i-1])
    b = [c=="1" for c in bin(i)[2:][::-1]]
    bl = len(b)
    for j in range(18):
        if j < xl: bits[i][j] = bits[i-1][j]
        if j < bl and b[j]: bits[i][j] += 1

print(bits[:10])

out = []
for _ in range(int(input())):
    l, r = map(int, input().split())
    bl = bits[l]
    br = bits[r]
    print(l, bl)
    print(r, br)
    components = [br[i]-bl[i] for i in range(18)]
    print(components)
    out.append(str(r+1-l-max(components)))

print("\n".join(out))

"""
0
1 1
2 01
3 11
4 001
5 101
6 011
111
0001
1001
0101
1101
0011
1011
0111
1111
00001
10001
01001






"""