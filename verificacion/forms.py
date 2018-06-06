from django import forms
import datetime

class InputForm(forms.Form):
    input = forms.CharField(label='Input', max_length=100)
    date = forms.DateField(label='Date', initial=datetime.date.today)