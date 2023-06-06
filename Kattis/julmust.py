R = int(input())
top = R+1
bottom = 0
for day in range(1, 86):

    mid = (top+bottom)//2

    print(mid*day, flush=True)
    response = input()

    if response == 'less':
        top = mid
    elif response == 'more':
        bottom = mid+1
    else:
        break
