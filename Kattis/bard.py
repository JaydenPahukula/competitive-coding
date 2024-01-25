n = int(input())
e = int(input())
people = set(range(1,n+1))
for _ in range(e):
    a = set(map(int, input().split()[1:]))
    if 1 in a:
        people &= a
    else:
        for person in a: people.add(person)
print("\n".join(map(str, sorted(list(people)))))