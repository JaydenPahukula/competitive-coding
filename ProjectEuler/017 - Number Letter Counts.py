def intToList(n):
    list = []
    reverse = []
    for i in str(n):
        list.append(int(i))
    for i in range(len(list)):
        reverse.append(list[-i-1])
    return reverse

def sumOfChars(n):
    sum = 0
    for i in range(1,n+1):
        list = intToList(i)
        while len(list) < 3:
            list.append(0)
        if len(list) == 4:
            sum += len("onethousand")
            continue
        if list[2] == 1:
            sum += len("onehundred")
        if list[2] == 2:
            sum += len("twohundred")
        if list[2] == 3:
            sum += len("threehundred")
        if list[2] == 4:
            sum += len("fourhundred")
        if list[2] == 5:
            sum += len("fivehundred")
        if list[2] == 6:
            sum += len("sixhundred")
        if list[2] == 7:
            sum += len("sevenhundred")
        if list[2] == 8:
            sum += len("eighthundred")
        if list[2] == 9:
            sum += len("ninehundred")

        if list[2] != 0 and (list[0] > 0 or list[1] > 0):
            sum += len("and")

        if list[1] == 9:
            sum += len("ninety")
        if list[1] == 8:
            sum += len("eighty")
        if list[1] == 7:
            sum += len("seventy")
        if list[1] == 6:
            sum += len("sixty")
        if list[1] == 5:
            sum += len("fifty")
        if list[1] == 4:
            sum += len("forty")
        if list[1] == 3:
            sum += len("thirty")
        if list[1] == 2:
            sum += len("twenty")
        if list[1] == 1:
            if list[0] == 9:
                sum += len("nineteen")
            if list[0] == 8:
                sum += len("eighteen")
            if list[0] == 7:
                sum += len("seventeen")
            if list[0] == 6:
                sum += len("sixteen")
            if list[0] == 5:
                sum += len("fifteen")
            if list[0] == 4:
                sum += len("fourteen")
            if list[0] == 3:
                sum += len("thirteen")
            if list[0] == 2:
                sum += len("twelve")
            if list[0] == 1:
                sum += len("eleven")
            if list[0] == 0:
                sum += len("ten")
        else:
            if list[0] == 9:
                sum += len("nine")
            if list[0] == 8:
                sum += len("eight")
            if list[0] == 7:
                sum += len("seven")
            if list[0] == 6:
                sum += len("six")
            if list[0] == 5:
                sum += len("five")
            if list[0] == 4:
                sum += len("four")
            if list[0] == 3:
                sum += len("three")
            if list[0] == 2:
                sum += len("two")
            if list[0] == 1:
                sum += len("one")
    return sum
            





print(sumOfChars(1000))
