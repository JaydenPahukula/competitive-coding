INFINITY = 6789
EPS = 0.00001
for _ in range(int(input())):
    x1,y1,x2,y2,x3,y3,x4,y4 = map(float, input().split())
    (x1,y1),(x2,y2) = sorted(((x1,y1),(x2,y2)))
    (x3,y3),(x4,y4) = sorted(((x3,y3),(x4,y4)))
    (x1,y1,x2,y2),(x3,y3,x4,y4) = sorted(((x1,y1,x2,y2),(x3,y3,x4,y4)))
    if x1 == x2:
        m1 = INFINITY
        b1 = x1
    else:
        m1 = (y1-y2)/(x1-x2)
        b1 = y1-(m1*x1)
    if x3 == x4:
        m2 = INFINITY
        b2 = x3
    else:
        m2 = (y3-y4)/(x3-x4)
        b2 = y3-(m2*x3)
    if m1 == INFINITY and m2 == INFINITY:
        if b1 == b2:
            if y2 < y3: print("none")
            elif y2 == y3: print("%.2f"%round(x2,2),"%.2f"%round(y2,2))
            else:
                (x1,y1),(x2,y2),(x3,y3),(x4,y4) = sorted(((x1,y1),(x2,y2),(x3,y3),(x4,y4)))
                print("%.2f"%round(x2,2),"%.2f"%round(y2,2),"%.2f"%round(x3,2),"%.2f"%round(y3,2))
        else:
            print("none")
        continue
    if m2 == INFINITY and m1 != INFINITY:
        x1,y1,x2,y2,x3,y3,x4,y4,m1,m2,b1,b2=x3,y3,x4,y4,x1,y1,x2,y2,m2,m1,b2,b1
    if m1 == INFINITY and m2 != INFINITY:
        if x3 <= x1 and x4 >= x1: print("%.2f"%round(x1,2),"%.2f"%round((m2*x1)+b2,2))
        else: print("none")
        continue
    if m1 == m2:
        if b1 == b2:
            if x2 == x3: print("%.2f"%round(x2,2), "%.2f"%round(y2,2))
            elif x2 < x3: print("none")
            else:
                (x1,y1),(x2,y2),(x3,y3),(x4,y4) = sorted(((x1,y1),(x2,y2),(x3,y3),(x4,y4)))
                print("%.2f"%round(x2,2),"%.2f"%round(y2,2),"%.2f"%round(x3,2),"%.2f"%round(y3,2))
        else:
            print("none")
    else:
        x = (b2-b1)/(m1-m2)
        if x+EPS >= x1 and x-EPS <= x2 and x+EPS >= x3 and x-EPS <= x4:
            print("%.2f"%round(x,2),"%.2f"%round((m1*x)+b1,2))
        else:
            print("none")
