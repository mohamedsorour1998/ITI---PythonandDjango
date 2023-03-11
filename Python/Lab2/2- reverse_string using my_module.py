# 2 - Create a custom Python module called my_module with a
# function that takes a string as input and returns the reverse of the
# string. Then write a Python program that imports the my_module
# module and uses the reverse_string function to reverse the string
# "Hello, world!".
from my_module import reverse_string

mystring = "Mohamed Sorour"
print("the reversed string is", reverse_string(mystring))
