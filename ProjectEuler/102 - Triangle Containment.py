

def solution(filepath:str):

    triangles = []
    with open(filepath, 'r') as f:
        s = f.readline()
        while len(s) != 0:
            triangles.append([int(x) for x in s.split(',')])
            s = f.readline()

    count = 0
    for t in triangles:
        s1 = (-t[2]) * (t[1]-t[3]) - (t[0]-t[2]) * (-t[3])
        s2 = (-t[4]) * (t[3]-t[5]) - (t[2]-t[4]) * (-t[5])
        s3 = (-t[0]) * (t[5]-t[1]) - (t[4]-t[0]) * (-t[1])
        s1 /= abs(s1)
        s2 /= abs(s2)
        s3 /= abs(s3)
        if s1 == s2 and s2 == s3:
            count += 1

    return count

print(solution("102 - triangles.txt"))
