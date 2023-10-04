import sys
input = sys.stdin.readline
output = []
while 1:

    na, nb = map(int, input().strip().split())
    if na == 0 and nb == 0: break
    a = set([int(input().strip()) for i in range(na)])
    count = 0
    for i in range(nb):
        if int(input().strip()) in a: count += 1
    output.append(count)

print("\n".join(map(str, output)))
