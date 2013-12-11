# Django forms model, "django-guestbook/guestbook/forms.py"
from django import forms
from guestbook.models import Greeting

class CreateGreetingForm(forms.ModelForm):
    class Meta:
        model = Greeting
        exclude = ('author', 'date') # same as "fields = ('content',)"
        
class CreateNewUserForm(forms.Form):
    username = forms.CharField(max_length = 30)
    password = forms.CharField(max_length = 30, widget=forms.PasswordInput)
    email = forms.CharField(max_length = 30)
    first_name = forms.CharField(max_length = 30)
    last_name = forms.CharField(max_length = 30)