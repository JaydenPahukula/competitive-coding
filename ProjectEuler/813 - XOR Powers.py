
def xorProduct(a:int, b:int):
    product = 0
    for i, bit in enumerate(str(bin(b))[:1:-1]):
        if int(bit):
            product = product ^ (a << i)
    return product

def solution(n:int):
    num = 11
    for i in range(n, 1, -1):
        #print(i)
        num = xorProduct(num, 11)
    return num % (10**9 + 7)

for i in range(1, 100, 2):
    s = solution(i)
    print(i, str(bin(s))[2:], s)