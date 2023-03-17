myStringList = ["hello", "from", "eng", "sorour"]
max = 0
for string in myStringList:
    if len(string) > max:
        max = len(string)

for string in myStringList:
    if len(string) == max:
        print(string)
