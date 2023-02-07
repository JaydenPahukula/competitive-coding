
def factorial(n:int):
    if n == 0 or n == 1: return 1
    product = 1
    for i in range(2, n+1):
        product *= i
    return product

def combanatoricSelections():
    count = 0
    for n in range(1,101):
        for r in range(1,n+1):
            c = factorial(n) / (factorial(r) * factorial(n - r))
            if c > 1000000:
                count += 1
    return count

print(combanatoricSelections())