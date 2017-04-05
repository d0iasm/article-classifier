from django import forms


class AdaptationForms(forms.Form):
    url = forms.URLField(
        label = 'Article URL',
        required = True
    )

class LearningForms(forms.Form):
    category = forms.CharField(
        label = 'category',
        required = True
    )
    url = forms.URLField(
        label = 'Article URL',
        required = True
    )
