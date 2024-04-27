n = int(input())
a = list(map(int, input().split()))

i = 0
j = n-1
s1 = a[i]
s3 = a[j]

best = 0
while i < j:
    if s1 == s3:
        best = s1
    if s1 <= s3:
        i += 1
        s1 += a[i]
    else:
        j -= 1
        s3 += a[j]

print(best)
