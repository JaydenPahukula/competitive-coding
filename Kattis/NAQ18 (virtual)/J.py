
def possibleJumps(y:int, x:int):
    if x > 4 or x < 0 or y > 4 or x < 0 or x > y:
        return "invalid coords"
    spots = []
    if x < y-1:
        spots.append((y-1, x, y-2, x))
        spots.append((y, x+1, y, x+2))
    if x > 1:
        spots.append((y-1, x-1, y-2, x-2))
        spots.append((y, x-1, y, x-2))
    if y < 3:
        spots.append((y+1, x, y+2, x))
        spots.append((y+1, x+1, y+2, x+2))
    return spots

def findMoves(board):
    boards = []
    for y in range(5):
        for x in range(y+1):
            if board[y][x]:
                for y1, x1, y2, x2 in possibleJumps(y, x):
                    if board[y1][x1] and not board[y2][x2]:
                        newBoard = [row.copy() for row in board]
                        score = newBoard[y][x] * newBoard[y1][x1]
                        newBoard[y2][x2] = newBoard[y][x]
                        newBoard[y][x] = 0
                        newBoard[y1][x1] = 0
                        boards.append((newBoard, score))
    return boards


startingBoard = []
for i in range(5):
    startingBoard.append(list(map(int, input().split())))

def bestScore(board):
    score = 0
    moves = findMoves(board)
    if moves:
        return max([score+newScore-bestScore(newBoard) for newBoard, newScore in moves])
    else:
        return 0

print(bestScore(startingBoard))