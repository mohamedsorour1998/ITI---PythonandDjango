# 7 - Write a Python program that reads a file named example.txt and
# removes all newline characters from the file.
with open("Lab2/example.txt", "r") as readFile:
    lines = readFile.readlines()
    lines = [line.replace("\n", "") for line in lines]
    print(lines)