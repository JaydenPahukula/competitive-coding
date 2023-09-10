n = int(input())
a = list(map(int, input().split()))
count = [0 for _ in range(4)]
for item in a:
    count[item] += 1
dp = [[[None for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)] 
dp[0][0][0] = 0

for c in range(n+1):
    for b in range(n+1):
        for a in range(n+1):
            if a+b+c == 0: continue
            if a+b+c > n: break
            zero = n-a-b-c
            result = zero/n
            if a: result += a/n*(dp[a-1][b][c]+1)
            if b: result += b/n*(dp[a+1][b-1][c]+1)
            if c: result += c/n*(dp[a][b+1][c-1]+1)
            result /= (1-zero/n)
            dp[a][b][c] = result
            if [0,a,b,c] == count:
                print(result)
                exit()