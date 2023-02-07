


def passcodeDerivation(fileName:str):

    #read from file
    with open(fileName, 'r') as file:
        log = file.readlines()
    file.close()

    #configure log
    for i in range(len(log)):
        log[i] = [int(log[i][0]), int(log[i][1]), int(log[i][2])]

    digits = []
    rules = []
    for i in range(len(log)):
        #get a list of all used digits
        for d in log[i]:
            if d not in digits:
                digits.append(d)
        #get a list of all rules
        for j in range(len(log[i])-1):
            r = log[i][j:j+2]
            if r not in rules:
                rules.append(r)


    numDigits = len(digits)
    passcode = [-1] * numDigits
    i = 0
    while 1:

        #find the next digit in the passcode
        nextDigit = digits.copy()
        for rule in rules:
            if rule[1] in nextDigit:
                nextDigit.remove(rule[1])

        #remove all rules using next digit
        rulesToRemove = []
        for rule in rules:
            if rule[0] == nextDigit[0]:
                rulesToRemove.append(rule)
        for rule in rulesToRemove:
            rules.remove(rule)
        
        #append next digit to passcode
        passcode[i] = nextDigit[0]
        digits.remove(nextDigit[0])

        #exit condition
        if len(rules) == 1:
            passcode[i+1] = rules[0][0]
            passcode[i+2] = rules[0][1]
            return passcode
        
        i += 1

    return "something went wrong :("

print(passcodeDerivation("079 - keylog.txt"))