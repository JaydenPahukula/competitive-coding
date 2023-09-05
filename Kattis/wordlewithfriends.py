ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n, w = map(int, input().split())
options = [{c for c in ALPHABET} for _ in range(5)]
knownMinCount = {letter:0 for letter in ALPHABET}
knownMaxCount = {letter:5 for letter in ALPHABET}
for _ in range(n):
    word, result = input().split()
    count = {letter:0 for letter in ALPHABET}
    done = {letter:False for letter in ALPHABET}
    for i in range(5):
        if result[i] == "G":
            options[i] = {word[i]}
            count[word[i]] += 1
        elif result[i] == "Y":
            if word[i] in options[i]: options[i].remove(word[i])
            count[word[i]] += 1
        else:
            if word[i] in options[i]: options[i].remove(word[i])
            done[word[i]] = True
    for l in ALPHABET:
        knownMinCount[l] = max(knownMinCount[l], count[l])
        if done[l]: knownMaxCount[l] = count[l]

for _ in range(w):
    word = input()
    letterCount = {letter:0 for letter in ALPHABET}
    for i, c in enumerate(word):
        if c not in options[i]: break
        letterCount[c] += 1
    else:
        for l in ALPHABET:
            if letterCount[l] < knownMinCount[l]: break
            if letterCount[l] > knownMaxCount[l]: break
        else:
            print(word)