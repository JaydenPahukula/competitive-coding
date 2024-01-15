for _ in range(int(input())):
    n,m = map(int, input().split())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()), reverse=True)
    total = 0
    for i in range(n):
        total += max(abs(b[i]-a[i]), abs(b[i+m-n]-a[i]))
    print(total)