for _ in range(int(input())):
    n, k = map(int, input().split())
    buffer = 0
    out = 0
    for c in input():
        if buffer:
            buffer -= 1
            continue
        if c == "B":
            buffer = k-1
            out += 1
    print(out)
