firstTime = True
while 1:
    n = int(input())
    if n == 0: break
    if not firstTime: print()
    firstTime = False
    stack = 2
    height = 0
    for _ in range(n):
        instruction, m = input().split()
        if instruction == "DROP":
            if stack == 1:
                print(f"MOVE 1->2 {height}")
                stack = 2
            print(f"DROP 2 {m}")
            height += int(m)
        elif instruction == "TAKE":
            if stack == 2:
                print(f"MOVE 2->1 {height}")
                stack = 1
            print(f"TAKE 1 {m}")
            height -= int(m)