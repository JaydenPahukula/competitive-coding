n = int(input())
prefixes = {}
for _ in range(n):
    word = input()
    if word in prefixes: print(prefixes[word])
    else: print(0)
    for i in range(1,len(word)+1):
        if word[:i] in prefixes: prefixes[word[:i]] += 1
        else: prefixes[word[:i]] = 1
