FATCPG = 9
PSSCPG = 4
ALCOHOLCPG = 7

totalTotal = .0
fatTotal = .0
done = False
while 1:
    raw = input()
    if raw != '-':
        done = False
        fat, protein, sugar, starch, alcohol = raw.split()

        cFat = 0
        cTotal = 0
        pFat = .0
        pTotal = .0

        #parse fat
        if fat[-1] == 'C':
            cFat += int(fat[:-1])
            cTotal += int(fat[:-1])
        elif fat[-1] == 'g':
            cFat += int(fat[:-1]) * FATCPG
            cTotal += int(fat[:-1]) * FATCPG
        else:
            pFat += int(fat[:-1]) / 100
            pTotal += int(fat[:-1]) / 100
        
        #parse protein, sugar, starch
        for x in [protein, sugar, starch]:
            if x[-1] == 'C':
                cTotal += int(x[:-1])
            elif x[-1] == 'g':
                cTotal += int(x[:-1]) * PSSCPG
            else:
                pTotal += int(x[:-1]) / 100
        
        #parse alcohol
        if alcohol[-1] == 'C':
            cTotal += int(alcohol[:-1])
        elif alcohol[-1] == 'g':
            cTotal += int(alcohol[:-1]) * ALCOHOLCPG
        else:
            pTotal += int(alcohol[:-1]) / 100
        
        #add to 
        foodTotal = cTotal / (1 - pTotal)
        totalTotal += foodTotal
        fatTotal += cFat + (foodTotal * pFat)
    
    else:
        if done == True: break
        done = True

        print(f"{int(100*fatTotal/totalTotal+0.5)}%")

        totalTotal = .0
        fatTotal = .0