# 14 - Write a function that takes a list of numbers as input and
# returns a new list containing the squares of each number in the
# input list.

import math

listOfNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def squaresOfEachNumberInTheList(listOfNumbers):
    myList = []
    for number in listOfNumbers:
        myList.append(math.sqrt(number))
    return myList


print(f"the square roots are {squaresOfEachNumberInTheList(listOfNumbers)}")
