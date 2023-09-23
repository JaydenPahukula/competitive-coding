m, n = map(int, input().split())
up = list(map(int, input().split()))
down = [x for x in up]
for i in range(1,m):
    up[i] += up[i-1]
    down[-i-1] += down[-i]
down = set(down)

up = [0]+up
down.add(0)
for _ in range(n):
    x = int(input())
    for i in range(m+1):
        if x > up[-1]: continue
        if x-up[i] in down:
            print("YES")
            break
    else:
        print("NO")