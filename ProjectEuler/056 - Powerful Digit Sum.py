
def powerfulDigitSum(n):
    maxDigits = 0
    for a in range(n):
        for b in range(n):
            c = a**b
            x = 0
            for char in str(c):
                x += int(char)
            if x > maxDigits:
                maxDigits = x
    return maxDigits

print(powerfulDigitSum(100))