n, w = input().split()
n = int(n)
d = {}
for _ in range(n):
    word, meanings = input().split()
    d[word] = int(meanings)

mem = {}
def numMeanings(s):
    if s == "": return 1
    if s in mem: return mem[s]
    meanings = 0
    for word in d:
        m = len(word)
        if len(s) < m: continue
        if s[:m] == word:
            meanings += d[word]*numMeanings(s[m:])
    mem[s] = meanings
    return meanings

print(numMeanings(w)%1000000007)