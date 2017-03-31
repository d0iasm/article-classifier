from django.shortcuts import render

import requests

from .lib.forms import AdaptationForms, LearningForms
from .lib.morpheme import Morpheme
from .lib.naivebayes import NaiveBayesClassifier
from .lib.training.training import Training

def index(request):
    form = AdaptationForms(request.POST or None)
    if form.is_valid():
        morpheme = Morpheme()
        res = requests.get(form.cleaned_data['url'])
        japanese_text = morpheme.filter(res.text)
        noun_list = morpheme.analysis(japanese_text)
        classifier = NaiveBayesClassifier()
        message = classifier.classifly(noun_list)
    else:
        message = 'ARTICLE URL'
    context = {
        'form': form,
        'message': message
    }
    return render(request, 'naivebayes/index.html', context)


def learn(request):
    form = LearningForms(request.POST or None)

    classifier = NaiveBayesClassifier()
    training = Training()
    message = training.get_data_count
    # if classifier.get_training_count < training.get_data_count:
    #     message = 'トレーニング未だ'
    # else:
    #     message = 'トレーニング終了'


    if form.is_valid():
        if 'action' in request.POST:
            morpheme = Morpheme()
            res = requests.get(form.cleaned_data['url'])
            japanese_text = morpheme.filter(res.text)
            noun_list = morpheme.analysis(japanese_text)
            category = form.cleaned_data['category']

            classifier.learn(category, noun_list)

        elif 'reset' in request.POST:
            classifier.reset()

    # message = classifier.get_training_count()

    context = {
        'form': form,
        'message': message
    }

    return render(request, 'naivebayes/learn.html', context)


def reset(request):
    pass
