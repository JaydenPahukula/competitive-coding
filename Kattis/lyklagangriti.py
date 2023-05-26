from collections import deque

before = deque()
after = deque()
for instruction in input():
    if instruction == "L":
        after.appendleft(before.pop())
    elif instruction == "R":
        before.append(after.popleft())
    elif instruction == "B":
        before.pop()
    else:
        before.append(instruction)
print("".join(before)+"".join(after))