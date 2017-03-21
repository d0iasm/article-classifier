from django.shortcuts import render

import requests

from .lib.forms import Forms
from .lib.naivebayes import *


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

def learn(request):
    training_data = [["good", [u"よい", u"とても"]],
                   ["good", [u"よい", u"とても", u"すばらしい"]],
                   ["good", [u"よい", u"すばらしい", u"見つかりません"]],
                   ["good", [u"すばらしい"]],
                   ["bad",  [u"見つかりません", u"買いたくない"]],
                   ["bad",  [u"よい"]],
                   ["bad",  [u"買いたくない", u"最悪"]],
                   ["bad",  [u"最悪"]]]

    # テスト用データ
    test_data  = [u"よい", u"とても"]

    classifier = NaiveBayesClassifier()

    # 学習フェーズ
    for c, f in training_data:
      classifier.learn(c, f)

    context = {
        'test': classifier.classifly(test_data)
    }
    
    return render(request, 'naivebayes/learn.html', context)
