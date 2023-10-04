s = input()
n = len(s)
nums = {"zero","one","two","three","four","five","six","seven","eight","nine"}
minLen = [9999999 for _ in range(n)]+[0]
ways = [1 for _ in range(n+1)]
for i in range(n-1,-1,-1):
    for cmp in nums:
        j = i+len(cmp)
        if i < n+1-len(cmp) and s[i:j] == cmp:
            if minLen[i] == minLen[j]+1: ways[i] += 1
            elif minLen[i] > minLen[j]+1:
                minLen[i] = minLen[j]+1
                ways[i] = ways[j]
        ways[i] %= 9302023
    if minLen[i] == minLen[i+1]+1: ways[i] += 1
    elif minLen[i] > minLen[i+1]+1:
        minLen[i] = minLen[i+1]+1
        ways[i] = ways[i+1]
    ways[i] %= 9302023
print(minLen[0])
print(ways[0])