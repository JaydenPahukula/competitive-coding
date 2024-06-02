q,w = map(int,input().split())
a = [0]*w
mountains = set()
for _ in range(q):
    x,y = map(int, input().split())
    add = 1
    # print(x,y,(x,y) in mountains)
    if (x,y) in mountains:
        mountains.remove((x,y))
        add = -1
    else:
        mountains.add((x,y))
    
    l,r = x-y,x+y
    for i in range(max(0,l),min(w,r)):
        a[i] += add
    
    count = 0
    for i in range(w):
        if a[i]: count += 1
    print("%.7f" % (count*(2**0.5)))
