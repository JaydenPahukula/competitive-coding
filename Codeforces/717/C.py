n = int(input())
a = list(map(int, input().split()))
A = []

mem = {}
def recursive(target, i):
    if (target,i) not in mem:
        result = True
        if target == 0: result = True
        elif i == 0: result = False
        else: result = recursive(target,i-1) or (A[i-1] <= target and recursive(target-A[i-1],i-1))
        mem[((target,i))] = result
    return mem[(target,i)]

def good(l:list):
    A.clear()
    for item in l: A.append(item)
    s = sum(l)
    if s%2: return True
    return not recursive(s//2, len(l))

# check with no removes
if good(a):
    print(0)
else:
    # check with 1 remove
    for i in range(n):
        if good(a[:i]+a[i+1:]):
            print(1)
            print(i+1)
            break
    else:
        # check with 2 removes
        for i in range(n):
            for j in range(i+1,n):
                if good(a[:i]+a[i+1:j]+a[j+1:]):
                    print(2)
                    print(i+1, j+1)
                    break
            else: continue
            break
