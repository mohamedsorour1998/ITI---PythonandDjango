# 5- Write a Python program that reads a file named example.txt and
# counts the number of lines in the file.
with open("Lab2/example.txt", "r") as file:
    nOL = len(file.readlines())
    print(nOL)