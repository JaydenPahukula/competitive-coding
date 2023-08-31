h, k, v, s = map(int, input().split())
x = 0
while h:
    v += s
    v -= max(1, v//10)
    if v >= k: h += 1
    if 0 < v and v < k:
        h -= 1
        if h == 0: v = 0
    if v <= 0: h, v = 0, 0
    x += v
    if s > 0: s -= 1
print(x)