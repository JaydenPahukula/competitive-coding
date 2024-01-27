from collections import deque
n = int(input())
s = input()
b = not n%2
d = deque()
for c in s:
    if b:
        d.appendleft(c)
    else:
        d.append(c)
    b = not b
print("".join(d))