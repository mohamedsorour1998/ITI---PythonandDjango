# 9 - Write a Python program that reads a file named example.txt and
# prints the longest word in the file.
with open("Lab2/example.txt", "r") as file:
    lines = file.readlines()
    myList = []
    max = 0
    for line in lines:
        for string in line.split():
            if len(string) > max:
                theLongestString = string
print(f"the longest string is: {theLongestString}")
