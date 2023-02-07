import math

def powerfulDigitCounts():
    count = 0
    for n in range(1, 10):
        for k in range(1, 22):
            if int(1 + k * math.log10(n)) == k:
                count += 1
    return count

print(powerfulDigitCounts())