for _ in range(int(input())):
    n, m = map(int, input().split())
    x = input()
    s = input()
    count = 0
    first = True
    while first or len(x) < 100:
        for i in range(n):
            #print(count, x[i:i+m], s)
            if x[i:i+m] == s:
                print(count)
                break
        else:
            x = x+x
            count += 1
            first = False
            continue
        break
    else:
        print(-1)
