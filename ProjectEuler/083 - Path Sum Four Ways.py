from queue import PriorityQueue

def solution(fileName:str, size:int):

    #read block
    block = []
    with open(fileName, 'r') as f:
        for i in range(size):
            line = [int(x) for x in (f.readline().split(','))]
            block.append(line)

    start = (0,0)
    end = (size-1,size-1)
    visited = {}
    q = PriorityQueue()
    q.put((0, start))
    
    while not q.empty():
        #get next best position
        (val, (y,x)) = q.get()

        #exit condition
        if (y,x) == end:
            return val+block[y][x]

        #if already visited
        if (y,x) in visited:
            continue
        else:
            visited[(y,x)] = val
        
        #add adjacent positions to queue
        if y >= 1 and y < size:
            q.put((val+block[y][x],(y-1,x)))
        if y >= 0 and y < size-1:
            q.put((val+block[y][x],(y+1,x)))
        if x >= 1 and x < size:
            q.put((val+block[y][x],(y,x-1)))
        if x >= 0 and x < size-1:
            q.put((val+block[y][x],(y,x+1)))

print(solution("083 - matrix.txt", 80))