from django.shortcuts import render

import requests

from .lib.forms import Forms


def index(request):
    form = Forms(request.POST or None)
    if form.is_valid():
        res = requests.get(form.cleaned_data['url'])
        message = res.text
    else:
        message = 'ARTICLE URL'
    context = {
        'form': form,
        'message': message
    }
    return render(request, 'naivebayes/index.html', context)
