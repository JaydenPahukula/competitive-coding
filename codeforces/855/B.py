from collections import defaultdict

for _ in range(int(input())):
    n, k = map(int, input().split())
    count = defaultdict(lambda: [0, 0])
    for c in input():
        count[c.lower()][c.isupper()] += 1
    score = 0
    for letter in count:
        if k > 0:
            while k > 0 and count[letter][0] > count[letter][1]+1:
                k -= 1
                count[letter][0] -= 1
                count[letter][1] += 1
            while k > 0 and count[letter][0]+1 < count[letter][1]:
                k -= 1
                count[letter][0] += 1
                count[letter][1] -= 1
        score += min(count[letter][0], count[letter][1])
    print(score)