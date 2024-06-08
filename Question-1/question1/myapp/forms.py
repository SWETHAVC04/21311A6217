from django import forms

class MyForm(forms.Form):
    numbers = forms.CharField(label='Enter 10 numbers:', max_length=100)