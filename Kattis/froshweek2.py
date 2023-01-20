
n, m = map(int, input().split(' '))
t = list(map(int, input().split(' ')))
l = list(map(int, input().split(' ')))

t.sort()
l.sort()

count = 0
for task in t[::-1]:
    if task <= l[-1]:
        l.pop()
        count += 1
        if len(l) == 0:
            break

print(count)