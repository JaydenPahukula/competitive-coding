for _ in range(int(input())):
    s = [list(input()), list(input())]
    n = len(s[0])
    t, q = map(int, input().split())
    blocked = [-t-1] * n
    for currt in range(q):
        inp = list(map(int, input().split()))
        queryType = inp[0]
        if queryType == 1:
            blocked[inp[1]-1] = currt
        elif queryType == 2:
            str1, pos1, str2, pos2 = inp[1:]
            s[str1-1][pos1-1], s[str2-1][pos2-1] = s[str2-1][pos2-1], s[str1-1][pos1-1]
        else:
            for i in range(n):
                #print(s[0][i], s[1][i], currt, blocked[i], currt-blocked[i] < t)
                if currt-blocked[i] < t: continue
                if s[0][i] != s[1][i]:
                    print("NO")
                    break
            else:
                print("YES")


