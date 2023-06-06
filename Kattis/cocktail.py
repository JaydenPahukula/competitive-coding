N, T = map(int, input().split())
a = [x-(T*i) for i, x in enumerate(sorted([int(input()) for _ in range(N)]))]
for x in a:
    if x <= 0:
        print("NO")
        break
else:
    print("YES")