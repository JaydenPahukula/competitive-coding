m = int(input())
n = int(input())
l = [int(input()) for _ in range(n)]

mem = {}
def f(target):
    if target == 0: return 1
    if target not in mem:
        count = 0
        for item in l:
            if item <= target: count += f(target-item)
        mem[target] = count
    return mem[target]

print(f(m))