
def solution(fileName:str, size:int):

    #read block
    block = []
    newBlock = []
    with open(fileName, 'r') as f:
        for i in range(size):
            line = [int(x) for x in (f.readline().split(','))]
            block.append(line)
            newBlock.append(line.copy())

    #find min path sum
    for x in range(1, size):
        for y in range(size):

            #determine all ways to get to (x, y) from (x-1, *)
            options = []
            for y1 in range(size):
                option = newBlock[y1][x-1]
                for y2 in range(y1+1, y+1):
                    option += block[y2][x-1]
                for y2 in range(y, y1):
                    option += block[y2][x-1]
                options.append(option)
            
            #take smallest option
            newBlock[y][x] += min(options)

    #return the smallest path from along the right side
    return min([newBlock[y][size-1] for y in range(size)])

print(solution("082 - matrix.txt", 80))