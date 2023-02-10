C = float(input())
total = 0
for _ in range(int(input())):
    l, w = map(float, input().split())
    total += l * w
print(C*total)