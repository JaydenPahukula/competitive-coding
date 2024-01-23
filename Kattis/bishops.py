import sys
for n in map(int, sys.stdin.readlines()):
    print(2*n-2 or 1)