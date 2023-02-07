

def checkComplete(puzzle):
    for row in puzzle:
        for num in row:
            if num == 0:
                return False
    return True

def solution(fileName:str, numPuzzles:int):
    total = 0

    #read puzzles
    p = [0] * 9
    puzzles = []
    with open(fileName, 'r') as f:
        for i in range(numPuzzles):
            f.readline()
            for j in range(9):
                p[j] = [int(x) for x in f.readline() if x != '\n']
            puzzles.append(p.copy())

    #solve each puzzle
    for puzzle in puzzles:
        #print("starting puzzle")
        checker = [[[] for i in range(9)] for j in range(9)]
        while 1:
            #print puzzle
            for row in puzzle:
                #print(row)
                pass
        
            #check if complete
            if checkComplete(puzzle):
                print("success!")
                total += 1
                break

            #update checker
            for y in range(9):
                for x in range(9):

                    nums = set([])

                    #check vertically
                    for y1 in range(9):
                        nums.add(puzzle[y1][x])
                    #check horizontally
                    for x1 in range(9):
                        nums.add(puzzle[y][x1])
                    #check 3x3 box
                    for by in range((y//3)*3, (y//3)*3+3):
                        for bx in range((x//3)*3, (x//3)*3+3):
                            nums.add(puzzle[by][bx])

                    #update checker
                    checker[y][x] = [x for x in range(1, 10) if x not in nums]

            #check single options
            done = False
            for y in range(9):
                for x in range(9):
                    if puzzle[y][x] == 0 and len(checker[y][x]) == 1:
                        puzzle[y][x] = checker[y][x][0]
                        done = True
                        break
                if done == True:
                    break
            if done == True:
                continue



            print("failed")
            break

        #print("done with puzzle")
                      


    return total

print(solution("096 - sudoku.txt",50))