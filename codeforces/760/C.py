for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mx = max(a)+1
    for d in range(2, mx):
        last = (a[0] % d == 0)
        for i in range(1, n):
            if (a[i] % d == 0) ^ last:
                last = (a[i] % d == 0)
            else:
                break
        else:
            print(d)
            break
    else:
        print('0')