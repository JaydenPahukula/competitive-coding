import sys
from collections import deque
input=sys.stdin.readline

out = []
for _ in range(int(input())):
    n = int(input())
    a = [c == "1" for c in input().strip()]

    for k in range(n,1,-1):
        toggle = 0
        toggleD = deque()
        for i in range(n-k+1):
            if not a[i]^toggle:
                toggle = 1-toggle
                toggleD.appendleft(i+k-1)
            if toggleD:
                front = toggleD.pop()
                if i == front: toggle = 1-toggle
                else: toggleD.append(front)
        for i in range(n-k+1,n):
            if not a[i]^toggle: break
            if toggleD:
                front = toggleD.pop()
                if i == front: toggle = 1-toggle
                else: toggleD.append(front)
        else:
            out.append(k)
            break
        continue
    else:
        out.append(1)

print("\n".join(map(str, out)))
