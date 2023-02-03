n = int(input())
books = []
for _ in range(n):
    books.append(int(input()))
total = 0
for i, price in enumerate(sorted(books)):
    if i % 3 != 0 or i > len(books)-2:
        total += price
print(total)
