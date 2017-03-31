from ..morpheme import Morpheme
from ..naivebayes import NaiveBayesClassifier

from . import data

class Training:

    def get_data_count(self):
        return len(data.training_data)
