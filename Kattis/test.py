import sys

def solve(ints, A, B, out):
    i = 0
    while i < len(ints) and ints[i][1] < A: i += 1
    while i < len(ints):
        mx = -1e10
        mxi = -1
        while i < len(ints) and ints[i][0] <= A:
            if ints[i][1] > mx:
                mx = ints[i][1]
                mxi = ints[i][2]
            i += 1
        if mxi == -1: return False
        out.append(mxi)
        A = mx
        if A >= B: return True
    return False

data = sys.stdin.readlines()
data.reverse()

while len(data) > 1:
    A, B = map(float, data.pop().split(' '))
    ints = []
    for i in range(int(data.pop())):
        a, b = map(float, data.pop().split(' '))
        ints.append((a, b, i))
    ints.sort()

    out = []
    if solve(ints, A, B, out):
        print(len(out))
        for num in out:
            print(num, end=' ')
        print()
    else:
        print("impossible")