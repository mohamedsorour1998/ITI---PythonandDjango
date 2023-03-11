# 6 - Write a Python program that reads a file named example.txt and
# prints the contents of the file in reverse order.
with open("Lab2/example.txt", "r") as file:
    content = file.read()
    reversedContent = content[::-1]
    print(reversedContent)