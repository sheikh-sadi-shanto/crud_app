from django import forms

# creating a form
class Form1(forms.Form):
    name = forms.CharField(max_length=12)
    img = forms.ImageField()