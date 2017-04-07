import requests

from ..morpheme import Morpheme
from ..naivebayes import NaiveBayesClassifier

from . import data


class Trainer:

    def get_data_count(self):
        return len(data.training_data)

    def training(self):
        morpheme = Morpheme()
        for one_data in data.training_data:
            res = requests.get(one_data[1])
            japanese_text = morpheme.filter(res.text)
            noun_list = morpheme.analysis(japanese_text)
            classifier = NaiveBayesClassifier()
            classifier.learn(one_data[0], noun_list)
