n = int(input())
houses = [tuple(map(int, input().split())) for _ in range(n)]
print(sum([x[1]-x[0] for x in houses])/n)