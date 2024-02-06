for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    mem = {}
    def dp(i,l):
        if i < 0: return 0
        if i not in mem:
            pass
        return mem[i]