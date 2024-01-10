for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    i = 0
    while k > 0:
        if i == n-1: break
        if a[i] == 0:
            i += 1
            continue
        a[i] -= 1
        a[-1] += 1
        k -= 1
    print(" ".join(map(str, a)))