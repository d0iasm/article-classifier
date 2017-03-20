from janome.tokenizer import Tokenizer

class Morpheme:
    def analysis(self):
        t = Tokenizer()
        for token in t.tokenize(u'すもももももももものうち'):
            print(token)

if __name__ == '__main__':
    morpheme = Morpheme()
    morpheme.analysis()
