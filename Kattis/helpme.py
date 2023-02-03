column = ['a','b','c','d','e','f','g','h']
pieces = ({'K':[],'Q':[],'R':[],'B':[],'N':[],'P':[]},{'K':[],'Q':[],'R':[],'B':[],'N':[],'P':[]})
for y in range(8):
    input()
    row = [x.strip(".:") for x in input().split('|')][1:-1]
    for x in range(8):
        c = row[x]
        if c == '': continue
        pieces[1-c.isupper()][c.upper()].append(column[x]+str(8-y))
input()
white = "White: "
black = "Black: "
for p in pieces[0].keys():
    pieces[0][p].sort(key=lambda x:x[1])
    for l in pieces[0][p]:
        white += p.replace("P","") + l + ","
    for l in pieces[1][p]:
        black += p.replace("P","") + l + ","
print(white[:-1])
print(black[:-1])
