
def gcd(a:int, b:int):
    while(b):
       a, b = b, a % b
    return abs(a)

def solution(L:int):
    bigList = [0 for i in range(L+1)]

    for n in range(1,100000):
        for m in range(n+1,100000):
            if (m+n) % 2 == 1 and gcd(m,n) == 1:

                a = (m**2)-(n**2)
                b = 2*n*m
                c = (m**2)+(n**2)
                total = a+b+c

                #if busted
                if total > L:
                    break

                #sieve
                for i in range(total, L+1, total):
                    bigList[i] += 1

    return sum([1 for x in bigList if x == 1])

print(solution(1500000))
