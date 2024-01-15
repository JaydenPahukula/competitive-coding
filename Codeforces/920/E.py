def check(h,w,xa,ya,xb,yb):
    if xa >= xb: return "Draw"
    # alice can win
    if (xb-xa) % 2 == 1:
        if abs(ya-yb) <= 1: return "Alice"
        if yb > ya and xb < xa+(w-ya)*2-1: return "Draw" # bob goes right
        if yb < ya and xb < xa+(ya-1)*2-1: return "Draw" # bob goes left
        return "Alice"
    # bob can win
    else:
        if ya == yb: return "Bob"
        if ya > yb and xa > xb-(w-yb)*2: return "Draw"  # alice goes right
        if ya < yb and xa > xb-(yb-1)*2: return "Draw"  # alice goes right
        return "Bob"

for _ in range(int(input())):
    h,w,xa,ya,xb,yb = map(int, input().split())
    print(check(h,w,xa,ya,xb,yb))