from django import forms
from services.models import *

class AddServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ('actual_rating')

class AddServiceReviewForm(forms.ModelForm):
    class Meta:
        model = ServiceReview
        exclude = ('date', 'service')