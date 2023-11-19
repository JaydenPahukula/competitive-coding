n=int(input())
lines=[input() for _ in range(n)]
a=set()
oof=set()
for i in range(n):
    if lines[i]=='Present!':
        a.add(lines[i-1])
    else:
        oof.add(lines[i])
s=oof-a

if len(s):print('\n'.join(sorted(s,key=lambda s:lines.index(s))))
else:print('No Absences')


