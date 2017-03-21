from janome.tokenizer import Tokenizer

import re
import nltk

class Morpheme:
    def filter(self, text):
       text = re.sub(r'[a-zA-Z0-9¥"¥.¥,¥@]+', '', text)
       text = re.sub(r'[!"“#$%&()\*\+\-\.,\/:;<=>?@\[\\\]^_`{|}~]', '', text)
       text = re.sub(r'[\n|\r|\t]', '', text)

       jp_chartype_tokenizer = nltk.RegexpTokenizer(u'([ぁ-んー]+|[ァ-ンー]+|[\u4e00-\u9FFF]+|[ぁ-んァ-ンー\u4e00-\u9FFF]+)')
       text = "".join(jp_chartype_tokenizer.tokenize(text))
       return text

    def analysis(self, text):
        noun_list = []
        t = Tokenizer()
        self.text = text
        for token in t.tokenize(self.text):
            part_of_speech = token.part_of_speech.split(',')[0]
            if part_of_speech == u'名詞':
                noun_list.append(token.surface)
        return noun_list

if __name__ == '__main__':
    morpheme = Morpheme()
    print(morpheme.analysis('[例]我輩は猫である。名前はまだ無い。'))
