import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = input()
    removed = [False for _ in range(n)]
    for i in range(2,n+1):
        if s[i-2:i+1] in ("pie","map") and not removed[i-2] and not removed[i-1]:
            removed[i] = True
    print(sum(removed))