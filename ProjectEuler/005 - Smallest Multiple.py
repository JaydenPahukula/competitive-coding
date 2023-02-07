i = 20*19

def checkIfMultiple(input):
    for n in range(1,21):
        if input % n != 0:
            return False
    return True

while 1:
    if checkIfMultiple(i):
        print(i)
        quit()
    i += 20*19