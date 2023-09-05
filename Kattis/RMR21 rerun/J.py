a = list(map(int, input().split()))
s = "ABC"

while 1:
    done = False
    # all forts are the same
    if a[0]==a[1] and a[1]==a[2]:
        print("Rubble!")
        break
    # one fort standing
    for i,j,k in [(0,1,2), (1,2,0), (2,0,1)]:
        if a[i] == 0 and a[j] == 0 and a[k] != 0:
            print(s[k], a[k])
            exit()
    # two forts standing
    for i,j,k in [(0,1,2), (1,2,0), (2,0,1)]:
        if a[i] == 0 and a[j] != 0 and a[k] != 0:
            if a[j] > a[k]: print(s[j], a[j]-a[k])
            else: print(s[k], a[k]-a[j])
            exit()
    # two equal and one -1
    for i,j,k in [(0,1,2), (1,2,0), (2,0,1)]:
        if a[i]==a[j] and a[k]==a[i]-1:
            print("Rubble!")
            exit()
    # two equal and one +1
    for i,j,k in [(0,1,2), (1,2,0), (2,0,1)]:
        if a[i]==a[j] and a[k]==a[i]+1:
            print(s[(i-a[k])%3], 1)
            exit()
    # two equal and one lower
    for i,j,k in [(0,1,2), (1,2,0), (2,0,1)]:
        if a[i] == a[j] and a[j] > a[k]:
            n = (a[j]-a[k])//3
            if n == 0: break
            a[i] -= 3*n
            a[j] -= 3*n
            done = True
            break
    if done: continue
    # two equal and one higher
    for i,j,k in [(0,1,2), (1,2,0), (2,0,1)]:
        if a[i] == a[j] and a[j] < a[k]:
            n = min(a[i]-1, (a[k]-a[j])//4)
            if n == 0: break
            a[i] -= n
            a[j] -= n
            a[k] -= 4*n
            done = True
            break
    if done: continue
    # 3 unequal
    for i,j,k in [(0,1,2), (0,2,1), (1,0,2), (1,2,0), (2,1,0), (2,0,1)]:
        if a[i] > a[j] and a[j] > a[k]:
            n = min(a[j]-a[k], a[i]-a[j])
            a[i] -= n*2
            a[j] -= n
            done = True
            break
    if done: continue
    # manual
    t0, t1, t3 = 0, 0, 0
    if a[2] > a[1]: t0 = 2
    else: t0 = 1
    if a[0] > a[2]: t1 = 0
    else: t1 = 2
    if a[1] > a[0]: t2 = 1
    else: t2 = 0
    a[t0] -= 1
    a[t1] -= 1
    a[t2] -= 1
