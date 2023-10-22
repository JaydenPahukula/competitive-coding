k = int(input())
nuggets = sorted(map(int, input().split()), reverse=True)
n = len(nuggets)
print(nuggets)
maxAmt = 0
for amt in range(20):
    count = 0
    used = set()
    for start in range(n):
        if start in used: continue
        print("starting with", nuggets[start])
        used.add(start)
        t = nuggets[start]
        while t < amt:
            for i in range(start+1,n):
                if i in used: continue
                if t + nuggets[i] <= amt:
                    t += nuggets[i]
                    print("added", nuggets[i])
                    used.add(i)
                    break
            else: t = 9**9
            break
        if t == amt:
            print("yes")
            count += 1
        else:
            print("no")
    print(amt, count)

print(maxAmt)
