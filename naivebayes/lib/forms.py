from django import forms


class AdaptationForms(forms.Form):
    url = forms.URLField(
        label = 'articleURL',
        required = True
    )

class LearningForms(forms.Form):
    category = forms.CharField(
        label = 'category',
        required = True
    )
    url = forms.URLField(
        label = 'articleURL',
        required = True
    )
