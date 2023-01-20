n = int(input())
words = [input() for _ in range(n)]
for i, word in enumerate(words):
    if i % 2 == 0:
        print(word)