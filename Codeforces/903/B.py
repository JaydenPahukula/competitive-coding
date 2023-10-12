for _ in range(int(input())):
    n = tuple(sorted(map(int, input().split())))
    s = sum(n)
    if n[1]%n[0]==0 and n[2]%n[0]==0 and s<=n[0]*6:
        print("YES")
    else:
        print("NO")