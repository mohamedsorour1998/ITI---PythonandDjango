# 15 - Write a function that takes an arbitrary number of lists as input
# using *args and returns a new list that contains all the elements
# from all the input lists.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
list4 = [10, 11, 12]
list5 = [13, 14, 15]


def newListThatContainsAllTheElementsFromTheInput(*args):
    myList = []
    for list in args:
        for element in list:
            myList.append(element)
    return myList


print(
    newListThatContainsAllTheElementsFromTheInput(list1, list2, list3, list4,
                                                  list5))
