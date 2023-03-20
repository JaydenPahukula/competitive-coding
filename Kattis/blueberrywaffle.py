r, f = map(int, input().split())
if (0.25 + f/(2*r)) % 1 > 0.5:
    print("down")
else:
    print("up")