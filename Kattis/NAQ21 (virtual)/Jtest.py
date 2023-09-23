from collections import deque
s = input().strip()
stack = deque()
for c in s:
    if c == "1": stack.append(1)
    elif c == "d": stack.append(stack[-1])
    else:
        add = stack.pop()+stack.pop()
        temp = deque()
        while stack:
            temp.append(stack.pop())
        while temp:
            new = temp.pop()-1
            if new: stack.append(new)
        stack.append(add)

while stack:
    print(stack.popleft(),end=" ")
print()
