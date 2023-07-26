def isPermutation(l:list):
    s = set()
    for item in l:
        if item < 1 or item > len(l): return False
        if item in s: return False
        s.add(item)
    return True

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    for i in range(n-2, 0, -1):
        l[i] -= l[i-1]

    if isPermutation(l) or isPermutation([1]+l):
        print("YES")
        continue

    l.sort()
    missing1 = -1
    missing2 = -1
    i = 0
    done = False
    for j in range(1, n+1):
        if l[i] != j:
            if missing1 == -1:
                missing1 = j
                i -= 1
            elif missing2 == -1:
                missing2 = j
                i -= 1
            else:
                if l[i] != missing1 + missing2:
                    print("NO")
                    break
                else:
                    done = True
        i += 1
    else:
        if done or (i == n-2 and missing1 != -1 and missing2 != -1 and l[-1] == missing1+missing2):
            print("YES")
        else:
            print("NO")