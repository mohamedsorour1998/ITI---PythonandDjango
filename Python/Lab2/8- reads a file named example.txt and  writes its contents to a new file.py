# 8 - Write a Python program that reads a file named example.txt and
# writes its contents to a new file named copy. txt.

with open("Lab2/example.txt", "r") as file:
    content = file.read()

with open("Lab2/copy.txt", "w") as file:
    file.write(content)