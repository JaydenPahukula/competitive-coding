def checkLeapYear(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        return False
    if year % 4 == 0:
        return True
    return False


def countSundays(startday,startmonth,startyear,endday,endmonth,endyear):
    referenceday = 1
    referencemonth = 1
    referenceyear = 1900
    referencedotw = 2
    leapyear = checkLeapYear(referenceyear)
    day = referenceday
    month = referencemonth
    year = referenceyear
    dotw = referencedotw
    sum = 0
    while True:
        if (year > startyear) or (year == startyear and month > startmonth) or (year == startyear and month == startmonth and day >= startday):
            if day == 1 and dotw == 1:
                sum += 1

        #end
        if day == endday and month == endmonth and year == endyear:
            return sum

        #increment day of the week
        dotw += 1
        if dotw == 8:
            dotw = 1
        #increment day
        day += 1
        if month in [4,6,9,11]:
            if day == 31:
                day = 1
                month += 1
        if month in [1,3,5,7,8,10,12]:
            if day == 32:
                day = 1
                month += 1
        if month == 2:
            if leapyear:
                if day == 30:
                    day = 1
                    month += 1
            else:
                if day == 29:
                    day = 1
                    month += 1
        if month == 13:
            month = 1
            year += 1
            leapyear = checkLeapYear(year)

        

print(countSundays(1,1,1901,31,12,2000))