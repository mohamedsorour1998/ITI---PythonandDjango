# 12 - Write a function that takes a dictionary as input and returns a
# new dictionary with the keys and values swapped (i.e., the keys
# become the values and the values become the keys)
dictionary = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}


def dictionaryWithTheKeysAndValuesSwapped(dictionary):
    myReversedDictionary = {}
    for k, v in dictionary.items():
        myReversedDictionary[v] = k
    return myReversedDictionary


print(dictionaryWithTheKeysAndValuesSwapped(dictionary))
