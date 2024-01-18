from math import comb

for _ in range(int(input())):
    n = int(input())
    l = sorted(map(int, input().split()))
    if n <= 2:
        print(0)
        continue

    c = [0]*(n+2)
    for x in l:
        c[x] += 1
    s = [0]*(n+2)
    s[0] = c[0]
    for i in range(1,n+2):
        s[i] = s[i-1]+c[i]

    count = 0
    for i in range(n+1):
        if i: count += comb(c[i],2)*s[i-1]
        count += comb(c[i],3)
    
    print(count)