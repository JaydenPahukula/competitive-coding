import math

w, h = map(int, input().split())
n, m = map(int, input().split())
asteroids = [tuple(map(int, input().split())) for _ in range(n)]

def isSafe(location:tuple):
    x, y = location
    for ax, ay, ar in asteroids:
        if ay-ar > y+h or ay+ar < y or ax-ar > x+w or ax+ar < x:
            continue
        if ay+ar >= y and ay-ar <= y+h and ax >= x and ax <= x+w:
            return False
        if ay >= y and ay <= y+h and ax+ar >= x and ax-ar <= x+w:
            return False
        for checky, checkx in [(y, x), (y+h, x), (y, x+w), (y+h, x+w)]:
            if math.hypot(checkx-ax, checky-ay) <= ar:
                return False
    return True

for _ in range(m):
    if isSafe(map(int, input().split())):
        print("DOOMSLUG GO!")
    else:
        print("DOOMSLUG STOP!")
