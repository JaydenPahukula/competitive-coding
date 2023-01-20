import sys

data = sys.stdin.readlines()
data.reverse()

while len(data) > 1:
    A, B = map(float, data.pop().split(' '))
    n = int(data.pop())
    intervals = []
    indexes = {}
    for i in range(n):
        a, b = map(float, data.pop().split(' '))
        if b > A and a < B:
            intervals.append((a, b))
            indexes[(a, b)] = i
    
    intervals.sort(key=lambda a: a[1])
    
    output = ""
    count = 0
    while 1:
        if A >= B:
            print(max(1, count))
            if output == "": output = "0"
            break

        maxb = A
        maxindex = -1
        for a, b in intervals:
            if a <= A and b > maxb:
                maxb = b
                maxindex = indexes[(a, b)]

        if maxindex == -1:
            output = "impossible"
            break
        
        while len(intervals) > 0 and intervals[0][1] <= maxb:
            intervals.pop(0)

        A = maxb
        count += 1
        output += str(maxindex) + " "
    
    print(output)