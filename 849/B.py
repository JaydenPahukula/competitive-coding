for _ in range(int(input())):
    input()
    y = 0
    x = 0
    for c in input():
        if c == 'U': y += 1
        elif c == 'R': x += 1
        elif c == 'D': y -= 1
        else: x -= 1
        if x == 1 and y == 1:
            break
    else:
        print("NO")
        continue
    print("YES")