from django import forms


class UrlForm(forms.Form):
    url = forms.URLField(
        label = 'article URL',
        required = True
    )
