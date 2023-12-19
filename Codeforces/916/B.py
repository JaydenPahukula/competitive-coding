for _ in range(int(input())):
    n, k = map(int, input().split())
    print(" ".join([str(x) for x in range(n-k, n+1)]+[str(y) for y in range(1,n-k)][::-1]))