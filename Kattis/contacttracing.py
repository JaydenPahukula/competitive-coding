import heapq

N,D = map(int, input().split())
C,*inf = list(map(int, input().split())); inf = set(inf)
people = [tuple(map(int, input().split()))+(i+1,i+1 in inf) for i in range(N)]
heapq.heapify(people)

safe = []
infected = []
contagious = []

output = []
for day in range(1, D+1):
    print("day", day, "=============")

    # infected people become contagious
    while infected:
        heapq.heappush(contagious, heapq.heappop(infected))

    # people enter room
    while people and people[0][0] == day:
        enter, leave, index, inf = heapq.heappop(people)
        if inf:
            output.append(index)
            heapq.heappush(contagious, (leave, index))
        else: heapq.heappush(safe, (leave, index))

    print(safe, infected, contagious)
    
    # if someone is contagious, everyone gets infected
    if len(contagious) > 0:
        while safe:
            person = heapq.heappop(safe)
            output.append(person[1])
            heapq.heappush(infected, person)

    # people leave room
    while safe and safe[0][0] == day:
        heapq.heappop(safe)
    while infected and infected[0][0] == day:
        heapq.heappop(infected)
    while contagious and contagious[0][0] == day:
        heapq.heappop(contagious)
print("hello")
print(" ".join(map(str, sorted(output))))

