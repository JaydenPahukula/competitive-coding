s = []

mem = {}
def dp(k:int, i, currGroup):
    print(" |"*i,k,i,currGroup)
    if k == 0 and i == len(s): return 0
    if k == 0 or i == len(s): return -123456789
    if (k,i,currGroup) not in mem:
        out = 0
        if sum(currGroup) > 0:
            win = 1 if currGroup[1]+int(s[i]==1) > currGroup[0]+int(s[i]==0) else 0
            if win: print(" |"*i,"win", sum(currGroup))
            out = max(out, win+dp(k-1,i+1,(int(s[i]==0),int(s[i]==1))))
        if s[i]:
            out = max(out, dp(k,i+1,(currGroup[0],currGroup[1]+1)))
        else:
            out = max(out, dp(k,i+1,(currGroup[0]+1,currGroup[1])))
        print(" |"*i,"done",out)
        mem[(k,i,currGroup)] = out
    return mem[(k,i,currGroup)]

for _ in range(int(input())):
    n = int(input())
    s = [c == "1" for c in input()]
    out = []
    for k in range(1,n+1):
        if k != 4: continue
        print("k =",k,"==========")
        out.append(dp(k,0,(0,0)))
        print("returned",out[-1])
    print(" ".join(map(str, out)))