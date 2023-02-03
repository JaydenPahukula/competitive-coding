x, y, n = map(int, input().split(' '))
for i in range(1, n+1):
    if i % x == 0 and i % y == 0:
        print("fizzbuzz")
    elif i % x == 0:
        print("fizz")
    elif i % y == 0:
        print("buzz")
    else:
        print(i)