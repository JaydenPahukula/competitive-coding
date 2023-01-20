h = 1
n = int(input())
while n-(h*h) >= 0:
    n -= h*h
    h += 2
print(int((h-1)/2))