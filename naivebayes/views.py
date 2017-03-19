from django.shortcuts import render

from .lib.forms import UrlForm


def index(request):
    form = UrlForm(request.POST or None)
    if form.is_valid():
        message = 'データ検証に成功しました'
    else:
        message = 'データ検証に失敗しました'
    context = {
        'hoge': 'world',
        'form': form,
        'message': message
    }
    return render(request, 'naivebayes/index.html', context)
