for _ in range(int(input())):
    n, a, b = map(int, input().split())
    s = input()
    if b >= 0: print(a*n+b*n)
    else:
        count = 0
        last = ""
        for c in s:
            if c != last:
                count += 1
            last = c
        print(a*n+b*((count+1)//2))