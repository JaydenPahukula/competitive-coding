for _ in range(int(input())):
    n, m, i1, j1, i2, j2, d = input().split()
    n, m, i1, j1, i2, j2 = map(int, [n, m, i1, j1, i2, j2])
    x = i1
    y = j1
    if d[0] == 'D': dx = 1
    else:           dx = -1
    if d[1] == 'R': dy = 1
    else:           dy = -1
    startingdx = dx
    startingdy = dy
    numBounces = 0
    i = 0
    while 1:
        if x == i2 and y == j2:
            print(numBounces)
            break
        if i > n*m*4 or (i > 0 and x == i1 and y == j1 and dx == startingdx and dy == startingdy):
            print("-1")
            break

        bounced = False

        x += dx
        if x < 1:
            bounced = True
            x = 2
            dx = 1
        elif x > n:
            bounced = True
            x = n-1
            dx = -1

        y += dy
        if y < 1:
            bounced = True
            y = 2
            dy = 1
        elif y > m:
            bounced = True
            y = m-1
            dy = -1
        
        if bounced: numBounces += 1
        i += 1