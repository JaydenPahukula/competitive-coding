n, s, r = map(int, input().split())
need = set(map(int, input().split()))
have = set(map(int, input().split()))
total = 0
for t in need:
    if t-1 in have: have.remove(t-1)
    elif t+1 in have: have.remove(t+1)
    else: total += 1
print(total)