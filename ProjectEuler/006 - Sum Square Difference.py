sumofsquares = 0
sum = 0
for i in range(1,101):
    sumofsquares += i**2
    sum += i
squareofsum = sum**2
print(squareofsum-sumofsquares)
