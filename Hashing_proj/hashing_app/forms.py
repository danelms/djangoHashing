from django import forms
from django.forms.widgets import Textarea

class HashForm(forms.Form):
    text = forms.CharField(label='Enter hash here:', widget=Textarea)