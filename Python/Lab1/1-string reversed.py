def stringReverse(text):
    return text[::-1]


print(stringReverse("i love coding"))

myString = "i love coding"
myStringList = myString.split(" ")
myStringList.reverse()
myReversedString = ' '.join(myStringList)
print(myReversedString)
