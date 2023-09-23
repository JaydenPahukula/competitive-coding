n = int(input())
l = list(map(int, input().split()))
instructions = []
x0 = 0
for item in l[::-1]:
    target = item+x0
    itemInstructions = []
    curr = 1
    x1 = 0
    partInstructions = ["1"]
    while curr < target:
        if curr*2 <= target:
            partInstructions.append("d")
            partInstructions.append("+")
            curr *= 2
            x1 += 1
        else:
            itemInstructions.append("+")
            itemInstructions.append("".join(partInstructions))
            partInstructions = ["1"]
            target += x1-curr
            x0 += x1+1
            curr = 1
            x1 = 0
    itemInstructions.append("".join(partInstructions))
    x0 += x1
    
    instructions.append("".join(itemInstructions[::-1]))
out = "".join(instructions[::-1])
print(out)


from collections import deque
s = out#input().strip()
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

# n = int(input())
# l = list(map(int, input().split()))
# instructions = []
# x0 = 0
# for item in l[::-1]:
#     target = item+x0
#     itemInstructions = []
#     parts = [i for i,c in enumerate(bin(target)[2:][::-1]) if c == "1"]
#     x1 = 0
#     for part in parts:
#         partTarget = part+x1
#         partInstructions = ["1"]
#         oldx1 = x1
#         x1 = 0
#         for _ in range(part):
#             partInstructions.append("d")
#             partInstructions.append("+")
#             x1 += 1
#         for _ in range(oldx1):
#             partInstructions.append("1")
#             partInstructions.append("+")
#             x1 += 1
#         if part != parts[-1]:
#             partInstructions.append("+")
#             x0 += 1
#         x0 += x1
#         itemInstructions.append(partInstructions)
#     instructions.append("".join(sum(itemInstructions[::-1],[])))
# print("".join(instructions[::-1]))