n, k = map(int, input().split())
l = sorted(list(map(int, input().split())))
maxOccurs = 0
maxK = 0
for i in range(n):
    occurs = 1
    count = 0
    for j in range(1,i+1):
        if count+(l[i]-l[i-j]) > k: break
        count += (l[i]-l[i-j])
        occurs += 1
    if occurs > maxOccurs:
        maxOccurs = occurs
        maxK = l[i]
print(maxOccurs, maxK)
