myInt = [5, 10, 15, 1, 19, 30, 7, 36, 4]


def largestNumInList(myInt):
    max = 0
    for num in myInt:
        if num > max:
            max = num
    return max


print("the largest number is: ", largestNumInList(myInt))
