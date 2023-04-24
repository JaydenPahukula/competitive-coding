for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    total = 0
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if a[j] % a[i] != 0: continue
            b = a[j]//a[i]
            for k in range(n):
                if k == i or k == j: continue
                if a[j]*b != a[k]: continue
                total += 1
    print(total)
