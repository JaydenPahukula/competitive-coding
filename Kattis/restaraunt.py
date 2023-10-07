while 1:
    n = int(input())
    if n == 0: break
    stack1 = 0
    stack2 = 0
    for _ in range(n):
        instruction, amount = input().split()
        amount = int(amount)
        if instruction == "DROP":
            stack2 += amount
            print(f"DROP 2 {amount}")
        else:
            initialTake = min(stack1, amount)
            if initialTake != 0:
                stack1 -= initialTake
                print(f"TAKE 1 {initialTake}")
            remaining = amount - initialTake
            if remaining != 0:
                print(f"MOVE 2->1 {stack2}")
                stack1, stack2 = stack2-remaining, 0
                print(f"TAKE 1 {remaining}")
    print()