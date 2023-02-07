
DEBUG = False

def findTriangles(d:int):
    nums = []
    n = 0
    while 1:
        num = int(n * (n + 1) / 2)
        n += 1
        if len(str(num)) == d:
            nums.append(num)
        elif len(str(num)) > d:
            return nums
def findSquares(d:int):
    nums = []
    n = 0
    while 1:
        num = n**2
        n += 1
        if len(str(num)) == d:
            nums.append(num)
        elif len(str(num)) > d:
            return nums
def findPentagons(d:int):
    nums = []
    n = 0
    while 1:
        num = int(n * (3* n - 1) / 2)
        n += 1
        if len(str(num)) == d:
            nums.append(num)
        elif len(str(num)) > d:
            return nums
def findHexagons(d:int):
    nums = []
    n = 0
    while 1:
        num = n * (2 * n - 1)
        n += 1
        if len(str(num)) == d:
            nums.append(num)
        elif len(str(num)) > d:
            return nums
def findHeptagons(d:int):
    nums = []
    n = 0
    while 1:
        num = int(n * (5 * n - 3) / 2)
        n += 1
        if len(str(num)) == d:
            nums.append(num)
        elif len(str(num)) > d:
            return nums
def findOctagons(d:int):
    nums = []
    n = 0
    while 1:
        num = n * (3 * n - 2)
        n += 1
        if len(str(num)) == d:
            nums.append(num)
        elif len(str(num)) > d:
            return nums

def findPolygon(set, cyclic:str):
    s = ""
    for i in set:
        if i != 0:
            s += "   "
    if s == "                  " and str(set[0])[:2] == cyclic:
        return [sum(set), set]
    if DEBUG: print(s, "set =", set)
    if set[1] == 0:
        squares = findSquares(4)
        if DEBUG: print(s, "checking squares...")
        for square in squares:
            if str(square)[:2] == cyclic:
                set[1] = square
                if DEBUG: print(s, "success! going deeper...")
                x = findPolygon(set, str(square)[2:])
                if x != []:
                    return x
                set[1] = 0
                if DEBUG: print(s, "set =", set)
        if DEBUG: print(s, "no squares")
    if set[2] == 0:
        pentagons = findPentagons(4)
        if DEBUG: print(s, "checking pentagons...")
        for pentagon in pentagons:
            if str(pentagon)[:2] == cyclic:
                set[2] = pentagon
                if DEBUG: print(s, "success! going deeper...")
                x = findPolygon(set, str(pentagon)[2:])
                if x != []:
                    return x
                set[2] = 0
                if DEBUG: print(s, "set =", set)
        if DEBUG: print(s, "no pentagons")
    if set[3] == 0:
        hexagons = findHexagons(4)
        if DEBUG: print(s, "checking hexagons...")
        for hexagon in hexagons:
            if str(hexagon)[:2] == cyclic:
                set[3] = hexagon
                if DEBUG: print(s, "success! going deeper...")
                x = findPolygon(set, str(hexagon)[2:])
                if x != []:
                    return x
                set[3] = 0
                if DEBUG: print(s, "set =", set)
        if DEBUG: print(s, "no hexagons")
    if set[4] == 0:
        heptagons = findHeptagons(4)
        if DEBUG: print(s, "checking heptagons...")
        for heptagon in heptagons:
            if str(heptagon)[:2] == cyclic:
                set[4] = heptagon
                if DEBUG: print(s, "success! going deeper...")
                x = findPolygon(set, str(heptagon)[2:])
                if x != []:
                    return x
                set[4] = 0
                if DEBUG: print(s, "set =", set)
        if DEBUG: print(s, "no heptagons")
    if set[5] == 0:
        octagons = findOctagons(4)
        if DEBUG: print(s, "checking octagons...")
        for octagon in octagons:
            if str(octagon)[:2] == cyclic:
                set[5] = octagon
                if DEBUG: print(s, "success! going deeper...")
                x = findPolygon(set, str(octagon)[2:])
                if x != []:
                    return x
                set[5] = 0
                if DEBUG: print(s, "set =", set)
        if DEBUG: print(s, "no octagons")
    if DEBUG: print(s, "failed")
    return []


def cyclicalFigurateNumbers():
    triangles = findTriangles(4)
    set = [0, 0, 0, 0, 0, 0]
    for triangle in triangles:
        cyclic = str(triangle)[2:]
        if DEBUG: print("triangle =", triangle)
        set[0] = triangle
        x = findPolygon(set, cyclic)
        if x != []:
            return x
    return "whelp, somethings not working :("

print(cyclicalFigurateNumbers())