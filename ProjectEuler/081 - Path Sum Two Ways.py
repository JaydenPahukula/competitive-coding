
def solution(fileName:str, size:int):

    #read block
    block = []
    with open(fileName, 'r') as f:
        for i in range(size):
            line = [int(x) for x in (f.readline().split(','))]
            block.append(line)

    #convert to diamond
    diamond = []
    for i in range(size * 2 - 1):
        line = []
        for j in range(max(0, i - size + 1), min(size, i+1)):
            line.append(block[i-j][j])
        diamond.append(line)

    #dp
    for y in range(1, len(diamond)):
        for x in range(len(diamond[y])):
            if x == 0 and y < size:
                diamond[y][x] += diamond[y-1][x]
            elif x == len(diamond[y])-1 and y < size:
                diamond[y][x] += diamond[y-1][x-1]
            elif y < size:
                diamond[y][x] += min(diamond[y-1][x], diamond[y-1][x-1])
            else:
                diamond[y][x] += min(diamond[y-1][x], diamond[y-1][x+1])

    return diamond[-1][0]

print(solution("081 - matrix.txt", 80))