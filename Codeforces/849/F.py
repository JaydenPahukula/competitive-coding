def update(num:int, n:int):
    if n == 0:
        return num
    elif n == 1:
        return sum([int(c) for c in str(num)])
    else:
        return sum([int(c) for c in str(update(num, n-1))])

for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0 for _ in a]
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            b[query[1]-1: query[2]] = [x+1 for x in b[query[1]-1: query[2]]]
        else:
            i = query[1]-1
            a[i] = update(a[i], b[i])
            b[i] = 0
            print("         ", a[i])
