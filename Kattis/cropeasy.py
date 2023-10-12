EPS = 0.0001

def isCenterInt(x1,y1,x2,y2,x3,y3):
    x = (x1+x2+x3)/3
    y = (y1+y2+y3)/3
    return abs(x-int(x+0.5)) < EPS and abs(y-int(y+0.5)) < EPS

for case in range(int(input())):
    n, A, B, C, D, x0, y0, M = map(int, input().split())
    trees = [(x0,y0)]
    for i in range(1,n):
        x0 = (A*x0+B)%M
        y0 = (C*y0+D)%M
        trees.append((x0,y0))
    
    count = 0
    for a in range(n):
        x1,y1 = trees[a]
        for b in range(a+1,n):
            x2,y2 = trees[b]
            for c in range(b+1,n):
                x3,y3 = trees[c]
                count += int(isCenterInt(x1,y1,x2,y2,x3,y3))
    print(f"Case #{case+1}:", count)