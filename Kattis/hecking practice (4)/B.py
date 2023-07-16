n, d = map(int, input().split())
a = [int(x)//d for x in input().split()]
count = 0
seen = {a[0]:1}
for i in range(1, n):
    if a[i] in seen:
        count += seen[a[i]]
        seen[a[i]] += 1
    else:
        seen[a[i]] = 1
    
print(count)