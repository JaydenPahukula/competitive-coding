import sys
o = []
for x in map(int,sys.stdin.readlines()):
    hi = 10**200
    lo = mid = 0
    while hi-lo > 0:
        mid = (hi+lo)//2
        cube = mid*mid*mid
        if cube == x: break
        if cube > x: hi = mid
        else: lo = mid+1
    ans = min(lo-1,lo,mid,hi,hi+1,key=lambda a:abs(a*a*a-x))
    o.append(ans)
        
print("\n".join(map(str,o)))
