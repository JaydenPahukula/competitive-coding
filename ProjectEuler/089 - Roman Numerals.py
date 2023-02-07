

def RNtoDEC(s:str):
    num = 0
    tracker = 0
    for c in s[::-1]:
        if c == 'I':
            if tracker == 0:
                num += 1
            else:
                num -= 1
        elif c == 'V':
            num += 5
            tracker = max([tracker, 1])
        elif c == 'X':
            if tracker <= 2:
                num += 10
            else:
                num -= 10
            tracker = max([tracker, 2])
        elif c == 'L':
            num += 50
            tracker = max([tracker, 3])
        elif c == 'C':
            if tracker <= 4:
                num += 100
            else:
                num -= 100
            tracker = max([tracker, 4])
        elif c == 'D':
            num += 500
            tracker = max([tracker, 5])
        elif c == 'M':
            num += 1000
            tracker = max([tracker, 6])
        else:
            return "invalid input"

    return num

def DECtoRN(num:int):
    s = ""
    while num >= 1000:
        s += "M"
        num -= 1000
    if num >= 900:
        s += "CM"
        num -= 900
    if num >= 500:
        s += "D"
        num -= 500
    elif num >= 400:
        s += "CD"
        num -= 400
    while num >= 100:
        s += "C"
        num -= 100
    if num >= 90:
        s += "XC"
        num -= 90
    if num >= 50:
        s += "L"
        num -= 50
    elif num >= 40:
        s += "XL"
        num -= 40
    while num >= 10:
        s += "X"
        num -= 10
    if num == 9:
        s += "IX"
        return s
    if num >= 5:
        s += "V"
        num -= 5
    elif num == 4:
        s += "IV"
        return s
    while num > 0:
        s += "I"
        num -= 1
    return s

def solution(filepath:str):
    diff = 0
    with open(filepath, 'r') as f:
        num = f.readline().replace('\n','')
        while len(num) != 0:
            diff += len(num) - len(DECtoRN(RNtoDEC(num)))
            num = f.readline().replace('\n','')
        
    return diff

print(solution("089 - roman.txt"))