from django import forms
from .models import Product, Report


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'content', 'starting_price', 'image', 'tags']


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'content', 'image', 'tags', 'status']


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title', 'content', 'image']
