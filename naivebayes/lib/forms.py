from django import forms


class Forms(forms.Form):
    url = forms.URLField(
        label = 'article URL',
        required = True
    )
