from django.forms import ChoiceField
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.db import models
from django.urls import reverse
from .models import Choice, Question
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import QuestionForm
from .forms import LoginForm
from django.contrib import messages
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm



# Create your views here.
def question_list(request):
    question_list = Question.objects.all()
    paginator = Paginator(question_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'questions': question_list}
    return render(request, 'polls/question_list.html', context)


def question_detail(request, pk):
    question = Question.objects.get(pk=pk)
    context = {'question': question}
    return render(request, 'polls/question_detail.html', context)


@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(
            reverse('polls:results', args=(question.id, )))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/results.html', context)


@login_required
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls:question_list')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'polls/question_create.html', context)


@login_required
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        question.delete()
        return redirect('polls:question_list')
    context = {'question': question}
    return render(request, 'polls/question_delete.html', context)


def Login_view(request):
    if request.user.is_authenticated:
     return redirect('polls:question_list')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('polls:question_list')

    else:
        form = AuthenticationForm()
    return render(request, 'polls/login.html', {'form': form})


def Logout_view(request):
    logout(request)
    return redirect('polls:question_list')


def Signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # authenticate the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            login(request, user)
            return redirect('polls:Login_view')
    else:
        form = UserCreationForm()
    return render(request, 'polls/signup.html', {'form': form})