from django.shortcuts import render

import requests

from .lib.forms import AdaptationForms, LearningForms
from .lib.morpheme import Morpheme
from .lib.naivebayes import NaiveBayesClassifier


def index(request):
    form = AdaptationForms(request.POST or None)
    if form.is_valid():
        morpheme = Morpheme()
        res = requests.get(form.cleaned_data['url'])
        japanese_text = morpheme.filter(res.text)
        message = morpheme.analysis(japanese_text)
    else:
        message = 'ARTICLE URL'
    context = {
        'form': form,
        'message': message
    }
    return render(request, 'naivebayes/index.html', context)

def learn(request):
    form = LearningForms(request.POST or None)

    if form.is_valid():
        if 'action' in request.POST:
            morpheme = Morpheme()
            res = requests.get(form.cleaned_data['url'])
            japanese_text = morpheme.filter(res.text)
            noun_list = morpheme.analysis(japanese_text)
            category = form.cleaned_data['category']
            # training_data = [category, noun_list]
            # training_data = [["good", [u"よい", u"とても"]],
            #                ["good", [u"よい", u"とても", u"すばらしい"]],
            #                ["good", [u"よい", u"すばらしい", u"見つかりません"]],
            #                ["good", [u"すばらしい"]],
            #                ["bad",  [u"見つかりません", u"買いたくない"]],
            #                ["bad",  [u"よい"]],
            #                ["bad",  [u"買いたくない", u"最悪"]],
            #                ["bad",  [u"最悪"]]]
            # テスト用データ

            test_data  = [u"よい", u"とても"]

            classifier = NaiveBayesClassifier()

            # # 学習フェーズ
            # TODO: ValueError:
            # too many values to unpack (expected 2)
            # for c, f in training_data:
            #   classifier.learn(c, f)
            classifier.learn(category, noun_list)

            # message = classifier.classifly(test_data)
            message = classifier.get_training_count()

        elif 'reset' in request.POST:
            message = 'リセット！'
    else:
        message = 'まだ！'

    context = {
        'form': form,
        'message': message
    }

    return render(request, 'naivebayes/learn.html', context)

def reset(request):
    pass
