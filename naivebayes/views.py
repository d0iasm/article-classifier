from django.shortcuts import render

from .lib.forms import UrlForm


def index(request):
    form = UrlForm(request.POST or None)
    if form.is_valid():
        # message = form.fields['url']
        message = form.cleaned_data['url']
    else:
        message = 'ARTICLE URL'
    context = {
        'form': form,
        'message': message
    }
    return render(request, 'naivebayes/index.html', context)
