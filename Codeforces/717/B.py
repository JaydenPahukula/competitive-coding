for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    target = 0
    for i in range(1,n):
        target ^= a[i-1]
        b = a[i:]
        curr = b.pop()
        while b:
            if curr == target:
                curr = b.pop()
            else:
                curr ^= b.pop()
        if curr == target:
            print("YES")
            break
        continue
    else:
        print("NO")