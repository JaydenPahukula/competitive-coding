for _ in range(int(input())):
    n, q = map(int, input().split())
    a = [int(x) % 2 for x in input().split()]
    total = sum(a)
    
    cumulative = [0 for _ in range(n+1)]
    for i in range(n):
        cumulative[i+1] = cumulative[i] + a[i]
    
    for _ in range(q):
        l, r, k = map(int, input().split())
        k = k % 2
        if (cumulative[l-1] + k*(r-l+1) + total-cumulative[r]) % 2 == 1:
            print("YES")
        else:
            print("NO")