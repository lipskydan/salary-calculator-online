from django import forms
from django.forms import widgets


class CalcMoneyForm(forms.Form):
    input_money = forms.FloatField(label='Input money', help_text='Input in UAH', localize=True,
                                   widget=widgets.TextInput(attrs={'size': 1, 'class': 'form-control'}))
