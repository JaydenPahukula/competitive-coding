t, n = map(int, input().split())
a = sorted(list(map(int, input().split())))
count = 0
for song in a:
    if count+song > t*60: break
    count += song
print(count)