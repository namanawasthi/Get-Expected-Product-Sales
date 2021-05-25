from django import forms
from . import models

class VotingForm(forms.Form):
    Choices = [
        ('Yes','Yes'),
        ('No','No')
        ]
    YourFeedBack = forms.ChoiceField(choices=Choices)
    
