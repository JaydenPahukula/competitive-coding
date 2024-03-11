import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline

for _ in range(int(input())):
    h,w,k,d = map(int,input().split())
    bridges = []
    for _ in range(h):
        a = list(map(int,input().split()))
        mem={}
        def dp(x,d1=d):
            if x == 0: return 1
            if x == w-1: return 1+dp(x-1,d)
            if (x,d1) not in mem:
                idk = a[x]+1+dp(x-1,d)
                if d1 > 0: idk = min(idk,dp(x-1,d1-1))
                mem[(x,d1)] = idk
            return mem[(x,d1)]
        bridges.append(dp(w-1))
    print(sum(sorted(bridges)[:k]))