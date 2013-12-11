from django import forms
from products.models import *

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('actual_rating')

class AddProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        exclude = ('author', 'date', 'product')