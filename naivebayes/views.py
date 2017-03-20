# coding: UTF-8

from django.shortcuts import render

import urllib.parse
import urllib.request
import requests

from .lib.forms import UrlForm


def index(request):
    form = UrlForm(request.POST or None)
    if form.is_valid():
        res = requests.get(form.cleaned_data['url'])
        # res = requests.post(form.cleaned_data['url'])
        # res.encoding = 'UTF-8'
        message = res.text

        # URLオブジェクト
        # message = form.fields['url']

        # クリーンなURL
        # message = form.cleaned_data['url']

        # url = form.cleaned_data['url']
        # values = {
        #     'charset': 'UTF-8'
        # }
        # data = urllib.parse.urlencode(values)
        # data = data.encode('utf-8')
        # with urllib.request.urlopen(urllib.request.Request(url, data)) as res:
        # with urllib.request.urlopen(form.cleaned_data['url']) as res:
            # message = res.read().decode('utf-8')
            # message = res.info().get_charset()
            # TODO: DjangoUnicodeDecodeError at /
            # 'utf-8' codec can't decode byte 0x90 in position 102:
            #  invalid start byte.
    else:
        message = 'ARTICLE URL'
    context = {
        'form': form,
        'message': message
    }
    return render(request, 'naivebayes/index.html', context)
