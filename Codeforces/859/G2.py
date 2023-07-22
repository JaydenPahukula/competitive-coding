for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    if a[0] != 1:
        print("NO")
        continue
    
    s = 1
    for i in range(1, n):
        if a[i] > s:
            print("NO")
            break
        s += a[i]
    else:
        print("YES")