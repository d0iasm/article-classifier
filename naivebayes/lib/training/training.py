import requests

from ..morpheme import Morpheme
from ..naivebayes import NaiveBayesClassifier

from . import data


class Training:

    def get_data_count(self):
        return len(data.training_data)

    def training(self):
        morpheme = Morpheme()
        for category in data.training_data:
            res = requests.get(category[1])
            # res = requests.get(form.cleaned_data['url'])
            japanese_text = morpheme.filter(res.text)
            noun_list = morpheme.analysis(japanese_text)
            # category = form.cleaned_data['category']
            classifier = NaiveBayesClassifier()
            classifier.learn(category[0], noun_list)
