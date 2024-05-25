n1,*e1 = map(int,input().split())
n2,*e2 = map(int,input().split())

def permutio(e):
    e.append(e[0])
    e.append(e[1])
    cols = [set() for _ in range(3001)]
    rows = [set() for _ in range(3001)]
    for i in range(0,len(e)-2,2):
        x1,y1 = e[i],e[i+1]
        x2,y2 = e[i+2],e[i+3]
        if x1 == x2:
            if y1 > y2: y1,y2 = y2,y1
            cols[x1].add((y1,y2))
        if y1 == y2:
            if x1 > x2: x1,x2 = x2,x1
            rows[y1].add((x1,x2))
    
    xo = [0 for _ in range(3001)]
    for x in range(1,3001): xo[x] = xo[x-1] + (1 if len(cols[x]) == 0 else 0)
    yo = [0 for _ in range(3001)]
    for y in range(1,3001): yo[y] = yo[y-1] + (1 if len(rows[y]) == 0 else 0)

    for x in range(3001):
        for y1,y2 in [_ for _ in cols[x]]:
            cols[x].remove((y1,y2))
            cols[x-xo[x]].add((y1-yo[y1],y2-yo[y2]))
        if xo[x]: cols[x].clear()
    for y in range(3001):
        for x1,x2 in [_ for _ in rows[y]]:
            rows[y].remove((x1,x2))
            rows[y-yo[y]].add((x1-xo[x1],x2-xo[x2]))
        if yo[y]: rows[y].clear()
    return rows,cols
    

def rot(rows,cols):
    maxY = 0
    for x in range(3001):
        for y1,y2 in cols[x]:
            maxY = max(maxY,y2)
    newCols = [set() for _ in range(3001)]
    newRows = [set() for _ in range(3001)]
    for xy in range(3001):
        for y1,y2 in cols[xy]:
            newRows[xy].add((maxY-y2,maxY-y1))
        for x1,x2 in rows[xy]:
            newCols[maxY-xy].add((x1,x2))
    return newRows,newCols


def check(rows1,cols1,rows2,cols2):
    for xy in range(3001):
        for line in rows1[xy]:
            if line not in rows2[xy]: return False
        for line in cols1[xy]:
            if line not in cols2[xy]: return False
    return True


r1,c1 = permutio(e1)
r2,c2 = permutio(e2)

if check(r1,c1,r2,c2):
    print("yes")
else:
    for _ in range(3):
        r1,c1 = rot(r1,c1)
        if check(r1,c1,r2,c2):
            print("yes")
            break
    else:
        print("no")
