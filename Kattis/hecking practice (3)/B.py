from math import sqrt, pow

def binet(n:int):
    phi = (1+sqrt(5))/2
    return ((pow(phi, n) - pow(-phi, n)) // sqrt(5)) % (10**9+7)

for _ in range(int(input())):
    n = int(input())
    print(binet(n+2))