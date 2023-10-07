from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
teque = [deque(), deque()]
out = []
for _ in range(n):
    instruction, x = input().split(); x = int(x)
    if instruction == "push_back":
        teque[1].append(x)
        if len(teque[1]) > len(teque[0]): teque[0].append(teque[1].popleft())
    elif instruction == "push_front":
        teque[0].appendleft(x)
        if len(teque[0]) > len(teque[1])+1: teque[1].appendleft(teque[0].pop())
    elif instruction == "push_middle":
        teque[1].appendleft(x)
        if len(teque[1]) > len(teque[0]): teque[0].append(teque[1].popleft())
    else:
        if x < len(teque[0]):
            out.append(teque[0][x])
        else:
            out.append(teque[1][x-len(teque[0])])
print("\n".join(map(str, out)))