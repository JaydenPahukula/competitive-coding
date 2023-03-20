def numOptions(targetLength:int, currLength:int=0):
    ways = 0
    for addedPiece in [1, 2, 3]:
        newLength = currLength + addedPiece
        if newLength > targetLength:
            pass
        elif newLength == targetLength:
            ways += 1
        else:
            ways += numOptions(targetLength, newLength)
    return ways

print(numOptions(int(input())))