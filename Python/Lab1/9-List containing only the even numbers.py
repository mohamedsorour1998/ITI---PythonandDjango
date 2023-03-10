myInt = [5, 10, 15, 1, 19, 30, 7, 36, 4]


def evenNumInList(myInt):
    evenList = []
    for num in myInt:
        if num % 2 > 0:
            evenList.append(num)
    return evenList


print("the even numbers in the list are: ", evenNumInList(myInt))
