
def xorProduct(a:int, b:int):
    bina = [int(x) for x in list(bin(a))[2:]]
    bina.reverse()
    #print(bina)
    l = []
    for i in range(len(bina)):
        if bina[i]:
            l.append(b << i)
    out = 0
    for item in l:
        out = out^item
    return out

def xorDivisors(n:int):
    
    #for every possible a and b
    for a in range(1, 2**(len(bin(n))-3)):
        for b in range(1, a+1):

            #check if their xor product == n
            binb = list(bin(b)[2:])
            x = 0
            for i in range(len(binb)):
                if binb[i] == '1':
                    x = x ^ (a << i)
            
            #exit condition
            if x == n:
                return [a, b]
        
    return "prime"

print(xorDivisors(4900001))
exit

def solution(n):
    primes = [i for i in range(3, n*1)]

print(solution(10))