m = int(input())
w = 0
h = 0
currw = 0
currh = 0
while 1:
    inp = list(map(int, input().split()))
    if inp == [-1, -1]:
        print(f"{w} x {h}")
        m = int(input())
        if m == 0: break
        w = 0
        h = 0
        currw = 0
        currh = 0
    else:
        w1, h1 = inp
        if w1 + currw > m:
            currw = w1
            currh = h
            h += h1
        else:
            currw += w1
            w = max(w, currw)
            h = max(h, currh+h1)