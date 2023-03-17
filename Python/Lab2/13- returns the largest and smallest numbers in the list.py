# 13 - Write a function that takes a list of numbers as input and
# returns the largest and smallest numbers in the list.

listOfNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def largestAndSmallestNumbersInTheList(listOfNumbers):
    max = 0
    min = 0
    myList = []
    for number in listOfNumbers:
        if number > max:
            max = number
        if number < min:
            min = number
    myList.append(max)
    myList.append(min)
    return myList


print(
    f"the largest number is {largestAndSmallestNumbersInTheList(listOfNumbers)[0]} and the smallest number is {largestAndSmallestNumbersInTheList(listOfNumbers)[1]}"
)
