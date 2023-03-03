from collections import defaultdict

def isNightmare(s1:str, s2:str):
    if len(s1) + len(s2) < 25: return False
    if len(set(s1+s2)) != 25: return False
    d = defaultdict(lambda: 0)
    for c in s1:
        d[c] += 1
    for c in s2:
        d[c] += 1
    for letter in d:
        if d[letter]%2 == 0: return False
    return True

n = int(input())
evens = []
odds = []
for i in range(n):
    s = input()
    if len(s)%2 == 0: evens.append(s)
    else: odds.append(s)

count = 0
for se in evens:
    for so in odds:
        if isNightmare(se, so): count += 1
print(count)