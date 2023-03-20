ds, ys = map(int, input().split())
dm, ym = map(int, input().split())
for day in range(1, 5001):
    if (day + ds) % ys == 0 and (day + dm) % ym == 0:
        print(day)
        break