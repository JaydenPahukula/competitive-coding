for _ in range(int(input())):
    a = sorted(map(int, input().split()), reverse=True)
    if a[0] + a[1] >= 10: print("YES")
    else:                 print("NO")