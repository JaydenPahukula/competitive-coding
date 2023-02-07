def digitSum(number):
    digits = []
    for n in str(number):
        digits.append(int(n))
    return(sum(digits))



print(digitSum(2**1000))