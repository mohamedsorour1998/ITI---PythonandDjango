vowels = ["a", "e", "i", "o", "u"]
string = input(
    "Please tell me the string so i tell you how many vowels in it: ")


def numberOfVowelsInTheString(string):
    counter = 0
    for char in string:
        for vowel in vowels:
            if vowel == char:
                counter = counter + 1
    return counter


print("the number of vowels in the given string is: ",
      numberOfVowelsInTheString(string))
