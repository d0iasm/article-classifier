from janome.tokenizer import Tokenizer

class Morpheme:
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
