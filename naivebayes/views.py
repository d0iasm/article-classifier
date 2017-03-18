from django.shortcuts import render


def index(request):
    context = {
        'hoge': 'world!'
    }
    return render(request, 'naivebayes/index.html', context)
