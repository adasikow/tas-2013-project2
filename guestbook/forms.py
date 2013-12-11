# Django forms model, "django-guestbook/guestbook/forms.py"
from django import forms
from guestbook.models import Greeting

class CreateGreetingForm(forms.ModelForm):
    class Meta:
        model = Greeting
        exclude = ('author', 'date') # same as "fields = ('content',)"