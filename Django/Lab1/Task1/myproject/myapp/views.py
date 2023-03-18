import math
import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
listOfRandomNames = ['Ahmed', 'Paul', 'George', 'Ringo']
listOfRandomNumbers = [1, 2, 3, 0]
# return the different "name" form the list each time the page is refreshed
def index(request):
    message = "Hello, " + listOfRandomNames[random.choice(listOfRandomNumbers)]
    return HttpResponse (message)