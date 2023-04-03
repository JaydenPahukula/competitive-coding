n, m = map(int, input().split())

a = [0 for _ in range(n)]
b = [0 for _ in range(m)]
for i in range(n):
    a[i] = int(input())
for i in range(m):
    b[i] = int(input())

a.sort()
b.sort()

wasted = 0
for num in b:

    #binary search (find closest)
    srt = 0
    end = n
    mid = (end+srt)//2
    closest = a[-1]
    while srt < end:
        if a[mid] == num:
            closest = a[mid]
            break
        if a[mid] < num:
            srt = mid+1
        else:
            closest = a[mid]
            end = mid
        mid = (end+srt)//2
    
    wasted += closest - num
print(wasted)