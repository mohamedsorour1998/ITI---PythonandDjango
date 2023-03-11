# 10 - Write a function that takes a list of integers as input and returns
# the sum of all even numbers in the list.
listOfIntegers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def theSumOfAllEvenNumbersInTheList(list):
    listOfEvenNumbers = []
    sum = 0
    for number in list:
        if number % 2 != 0:
            listOfEvenNumbers.append(number)
    for evenNumber in listOfEvenNumbers:
        sum = sum + evenNumber
    return sum


print(
    f" the Sum Of All Even Numbers In The List: {theSumOfAllEvenNumbersInTheList(listOfIntegers)}"
)
