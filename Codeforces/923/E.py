for _ in range(int(input())):
    n,k = map(int, input().split())
    a = n
    b = 1
    out = [None for _ in range(n)]
    for i in range(k):
        if i % 2:
            for j in range(i,n,k):
                out[j] = b
                b += 1
        else:
            for j in range(i,n,k):
                out[j] = a
                a -= 1
    print(" ".join(map(str, out)))
