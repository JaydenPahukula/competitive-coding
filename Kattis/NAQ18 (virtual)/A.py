n = int(input())
cards = []
for _ in range(n-1):
    cards.append([set(map(int, input().split())) for _ in range(5)])
    input()
cards.append([set(map(int, input().split())) for _ in range(5)])

def checkTie(a, b, i, j):
    sequence = cards[a][i].symmetric_difference(cards[b][j])
    for card in cards:
        if card == a or card == b: continue
        for row in card:
            if row.issubset(sequence): return False
    return True

for a in range(n-1):
    for b in range(a+1, n):
        for i in range(5):
            for j in range(5):
                if cards[a][i].union(cards[b][j]):
                    # possible tie, check:
                    if checkTie(a, b, i, j):
                        print(a+1, b+1)
                        exit()
print("no ties")
