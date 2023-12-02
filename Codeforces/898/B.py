for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    a[0] += 1
    out = 1
    for x in a: out *= x
    print(out)