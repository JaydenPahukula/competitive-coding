n, q = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = [True for _ in range(n)]
a.append(-1)

# n = int(input())
# a = list(map(int, input().split()))
# a.append(-1)

def binSearch(target:int):
    start = 0
    end = len(a)
    closest = a[-1]
    while start < end:
        mid = (end+start)//2
        if a[mid] == target:
            closest = mid
            break
        if a[mid] < target:
            start = mid+1
        else:
            closest = mid
            end = mid
    return closest
        
# while 1:
#     x = int(input("search for: "))
#     print(binSearch(x+1))
#     print(binSearch(x))

for _ in range(q):
    t, d = map(int, input().split())

    if t == 1:
        toRemove = binSearch(d+1)
    else:
        toRemove = binSearch(d)

    if toRemove != -1:
        print(a[toRemove])
        a.pop(toRemove)
    else:
        print(-1)
    
