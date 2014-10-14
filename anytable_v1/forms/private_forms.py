from django import forms

class DocumentForm(forms.Form):
    title = forms.CharField()
    file = forms.ImageField()