from django.shortcuts import render

from naivebayes.lib.forms import UrlForm


def index(request):
    context = {
        'hoge': 'world',
        'form': UrlForm,
    }
    return render(request, 'naivebayes/index.html', context)
