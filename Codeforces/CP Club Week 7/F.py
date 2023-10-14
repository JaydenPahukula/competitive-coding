import sys
input = sys.stdin.readline

output = []
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    options = sorted([[i,a[i],b[i]] for i in range(n)], key=lambda x: (x[1],-x[2]))
    for i in range(n-2,-1,-1): options[i][2] += options[i+1][2]
    for i in range(n): options[i][2] -= b[options[i][0]]
    options.append([-1,0,sum(b)])
    
    output.append(str(min([max(a,b) for i,a,b in options])))
print("\n".join(output))