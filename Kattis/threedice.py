from collections import deque

def check(x:list):
    d1, d2, d3 = x
    if len(d1) > 6 or len(d2) > 6 or len(d3) > 6: return False
    if d1 & d2 or d2 & d3 or d3 & d1: return False
    return True

n = int(input())
options = deque()
first = [set([c]) for c in input()]
if check(first): options.append(first)
for _ in range(n-1):
    c1, c2, c3 = input()
    numOptions = len(options)
    for _ in range(numOptions):
        d1, d2, d3 = options.popleft()
        if check([d1|{c1},d2|{c2},d3|{c3}]): options.append([d1|{c1},d2|{c2},d3|{c3}])
        if check([d1|{c1},d2|{c3},d3|{c2}]): options.append([d1|{c1},d2|{c3},d3|{c2}])
        if check([d1|{c2},d2|{c1},d3|{c3}]): options.append([d1|{c2},d2|{c1},d3|{c3}])
        if check([d1|{c2},d2|{c3},d3|{c1}]): options.append([d1|{c2},d2|{c3},d3|{c1}])
        if check([d1|{c3},d2|{c1},d3|{c2}]): options.append([d1|{c3},d2|{c1},d3|{c2}])
        if check([d1|{c3},d2|{c2},d3|{c1}]): options.append([d1|{c3},d2|{c2},d3|{c1}])
if options:
    final = options.pop()
    used = final[0] | final[1] | final[2]
    currLetter = 97
    for d in (final):
        while len(d) < 6:
            while chr(currLetter) in used:
                currLetter += 1
            d.add(chr(currLetter))
            used.add(chr(currLetter))
    print(" ".join(["".join(d) for d in (final)]))
else:
    print(0)