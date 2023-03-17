# 16 - Write a function that takes a string as input and an arbitrary
# number of keyword arguments using **kwargs. The function should
# replace all instances of the keyword argument keys in the input
# string with their corresponding values.


def newListThatContainsAllTheElementsFromTheInput(**kwargs):
    myList = []
    for k, v in kwargs.items():
        myList.append(k)
        myList.append(v)

    return myList


print(
    newListThatContainsAllTheElementsFromTheInput(job="engineer",
                                                  name="sorour"))
