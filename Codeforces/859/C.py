def check(s):
    currbit = 0
    known = (set(), set())
    for c in s:
        if c in known[currbit]:
            pass
        elif c in known[1-currbit]:
            return False
        else:
            known[currbit].add(c)
        currbit = 1-currbit
    return True


for _ in range(int(input())):
    n = int(input())
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
