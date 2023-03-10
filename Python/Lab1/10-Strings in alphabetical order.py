myStringList = ["hello", "from", "eng", "sorour"]


def stringsInAlphabeticalOrder(myStringList):
    myStringList.sort()
    return myStringList


print("the strings in alphabetical order : ",
      stringsInAlphabeticalOrder(myStringList))