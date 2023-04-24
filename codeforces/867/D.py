
def ispermutation(a:list):
    return sorted(a) == list(range(1, len(a)+1))

def superpermutation(a:list):
    n = len(a)
    b = [sum(a[:i+1]) % n + 1 for i in range(n)]
    return b

for _ in range(int(input())):
    n = int(input())
    
    l = list(range(1, n+1))