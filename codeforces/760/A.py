def check(l:list):
    l.sort()
    for i in range(5):
        for j in range(i+1, 6):
            for k in range(j+1, 7):
                a = l[i]
                b = l[j]
                c = l[k]
                newList = sorted([a, b, c, a+b, b+c, c+a, a+b+c])
                if newList == l:
                    return (a, b, c)
    return False


for _ in range(int(input())):
    b = list(map(int, input().split()))
    print(' '.join(map(str, check(b))))