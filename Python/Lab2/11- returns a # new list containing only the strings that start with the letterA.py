# 11 - Write a function that takes a list of strings as input and returns a
# new list containing only the strings that start with the letter "a".

ListOfStrings = [
    "hello", "my", "name", "is", "sorour", "and", "i", "am", "an", "engineer"
]


def stringsThatStartWithTheLetterA(ListOfStrings):
    ListOfStringsThatStartWithTheLetterA = []
    for string in ListOfStrings:
        if string.startswith("a") or string.startswith("A"):
            ListOfStringsThatStartWithTheLetterA.append(string)
    return ListOfStringsThatStartWithTheLetterA


print(stringsThatStartWithTheLetterA(ListOfStrings))