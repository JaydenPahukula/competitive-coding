
def isWeekend(day:int):
    return (day % 7 == 0) or (day % 7 == 6)

def checkAvailability(numMovers:int, dates:list, weekends:bool=False):
        availability = [numMovers for _ in range(max([date[1] for date in dates])+1)]
        dates.sort()
        #for each job
        for start, end in dates:
            actualStart = start
            while actualStart <= end:
                if (not weekends and isWeekend(actualStart)) or availability[actualStart] < 2:
                    #cannot start now, try to start tomorrow
                    actualStart += 1
                else:
                    #can start now, book em
                    availability[actualStart] -= 2
                    break
            else:
                #couldn't get the job done in time
                return False
        return True

for _ in range(int(input())):
    m, p = map(int, input().split())
    dates = [tuple(map(int, input().split())) for _ in range(m)]

    if checkAvailability(p, dates):
        print("fine")
    elif checkAvailability(p, dates, weekends=True):
        print("weekend work")
    else:
        print("serious trouble")
