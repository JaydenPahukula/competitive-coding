for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(1,n-1):
        a[i+1] -= a[i-1]
        a[i] -= 2*a[i-1]
        a[i-1] = 0
        print(a)
        if a[i] < 0 or a[i+1] < 0: break
    else:
        if sum(a): print("NO")
        else: print("YES")
        continue
    print("NO")