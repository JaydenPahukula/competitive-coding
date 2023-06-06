
def check(a:list):
    if min(a) % 2 == 0:
        for i in range(0, n):
            if a[i] % 2 == 1: return False
    return True

for _ in range(int(input())):
    n = int(input())
    if check(list(map(int, input().split()))):
        print("YES")
    else:
        print("NO")
        