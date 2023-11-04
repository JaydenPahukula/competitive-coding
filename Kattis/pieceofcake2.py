a,b,c = map(int, input().split())
print(max(b*c, (a-b)*c, b*(a-c), (a-b)*(a-c))*4)