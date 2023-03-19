from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['question_text']
        labels = {'question_text': 'Question'}
# this method is used to add validation to the form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['question_text'].widget.attrs.update(
            {'class': 'form-control'})

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)