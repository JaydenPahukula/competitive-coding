n = int(input())
d = float(input())
cars = [(0.0, "") for _ in range(n)]
for i in range(n):
    name, velocity, fuel = input().split()
    cars[i] = (1/float(fuel), name)
cars.sort()
print(cars[-1][1])