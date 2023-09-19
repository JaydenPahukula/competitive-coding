L, W = map(int, input().split())
traffic = [tuple(map(int, input().split())) for _ in range(L)]

def safe(x, y, t):
    if y == -1 or y >= L: return True
    if y%2: x = W-x-1
    offset, interval, speed = traffic[y]
    offset = (offset+t*speed)%interval
    mspeed = max(1, speed)
    x %= interval
    if x <= offset and x >= offset-mspeed+1: return False
    if x >= interval+offset-mspeed+1: return False
    return True

P, s = input().split()
x, y = int(P), L
for t, c in enumerate(s):
    if c == "U": y -= 1
    if c == "D": y += 1
    if c == "L": x -= 1
    if c == "R": x += 1
    if not safe(x, y, t+1):
        print("squish")
        break
else:
    if y == -1: print("safe")
    else: print("squish")



# for t in range(5):
#     for y in range(-1, L+1):
#         print(["O" if safe(x,y,t) else "X" for x in range(W)])
#     print()