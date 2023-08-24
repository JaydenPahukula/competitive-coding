N = int(input())
print(sum([a*b for a, b in [map(float, input().split()) for _ in range(N)]]))