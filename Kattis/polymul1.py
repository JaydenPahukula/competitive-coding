for _ in range(int(input())):
    n1 = int(input())
    a1 = list(map(int, input().split()))
    n2 = int(input())
    a2 = list(map(int, input().split()))
    a = [0 for _ in range(n1+n2+1)]
    for i1 in range(n1+1):
        for i2 in range(n2+1):
            a[i1+i2] += a1[i1]*a2[i2]
    print(n1+n2)
    print(' '.join(map(str, a)))