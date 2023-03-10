number = int(input("Please tell me the number: "))


def checkNumber(number):
    if number > 0:
        return "the number is positive"
    elif number < 0:
        return "the number is negative"
    elif number == 0:
        return "the number is zero"


print(checkNumber(number))
