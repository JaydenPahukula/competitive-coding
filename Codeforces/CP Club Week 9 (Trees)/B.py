n = int(input())
d = {"polycarp":1}
for _ in range(n):
    n1,n2 = input().split(" reposted ")
    n1,n2 = n1.lower(),n2.lower()
    d[n1] = d[n2]+1
print(max(d.values()))
