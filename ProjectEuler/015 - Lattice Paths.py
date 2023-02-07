
def permuteList(l):
    list = l
    listoflists = []
    if len(list) == 1:
        return [list]
    for i in range(len(list)):
        list[i], list[0] = list[0], list[i]
        for x in permuteList(list[1:]):
            listoflists.append([list[0]]+x)
        list[i], list[0] = list[0], list[i]
    return listoflists


def latticePaths(w,h):
    default = []
    for i in range(h):
        default.append(0)
    for i in range(w):
        default.append(1)
    return len(permuteList(default))



print(latticePaths(4,4))