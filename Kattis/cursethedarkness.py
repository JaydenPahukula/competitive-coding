from math import hypot
for _ in range(int(input())):
    x,y = map(float, input().split())
    n = int(input())
    candles = [tuple(map(float, input().split())) for _ in range(n)]
    for cx, cy in candles:
        if hypot(x-cx, y-cy) <= 8.00000001:
            print("light a candle")
            break
    else:
        print("curse the darkness")