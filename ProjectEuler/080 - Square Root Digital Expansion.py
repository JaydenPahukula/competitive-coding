import decimal as d

def solution():
    d.getcontext().prec = 102

    total = 0
    for i in range(1, 100):
        n = d.Decimal(i)
        if int(n.sqrt()) == n.sqrt():
            continue
        for digit in [int(x) for x in str(n.sqrt())[:101] if x != '.']:
            total += digit
    return total

print(solution())