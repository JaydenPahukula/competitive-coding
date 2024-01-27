from math import log
for _ in range(int(input())):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))

    def check():
        if max(a) == 0: return ("YES")
        for i in range(int(log(max(a),k))+1):
            count = 0
            for j in range(n):
                count += a[j]//(k**i)%k
            if count > 1: return "NO"
        return ("YES")    
    
    print(check())
