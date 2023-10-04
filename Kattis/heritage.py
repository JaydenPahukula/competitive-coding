# n, w = input().split()
# n = int(n)
# d = {}
# for _ in range(n):
#     word, meanings = input().split()
#     d[word] = int(meanings)

# mem = {}
# def numMeanings(s):
#     if s == "": return 1
#     if s in mem: return mem[s]
#     meanings = 0
#     for word in d:
#         m = len(word)
#         if len(s) < m: continue
#         if s[:m] == word:
#             meanings += d[word]*numMeanings(s[m:])
#     mem[s] = meanings
#     return meanings

# print(numMeanings(w)%1000000007)



N,W=input().split();d={a:int(b)for a,b in[input().split()for _ in "_"*int(N)]};c={"":1};L=len
def f(s):
 if s not in c:c[s]=sum([d[w]*f(s[L(w):])for w in d if s[:min(L(w),L(s))]==w])
 return c[s]
print(f(W)%1000000007)