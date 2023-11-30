
def properDivs(n:int):
    if n == 0 or n == 1: return []
    output = {1}
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            output.add(i)
            output.add(n//i)
    return list(output)

n = int(input())

curr = n
for i in range(32):
    curr = sum(properDivs(curr))
    if curr == n:
        print("looking down a barrel")
        break
else:
    print("safe from harm")