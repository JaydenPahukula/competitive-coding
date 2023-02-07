
def solution():

    n = int(input())
    for i in range(n):
        a, b = map(int, input().split(' '))
        if a % 2 == b % 2:
            print("Tonya")
        else:
            print("Burenka")

    return

solution()
