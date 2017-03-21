import math
import sys
from collections import defaultdict

class Feature:
    """ Feature for NaiveBayes"""

    def __init__(self, name):
        self.name = name
        self.categories = defaultdict(int)

    def __getitem__(self, category):
        return self.categories[category]

    def __setitem__(self, category, value):
        self.categories[category] = value


class NaiveBayesClassifier:
    """ NaiveBayes """

    def __init__(self):

        # 各カテゴリのデータの数
        self.categories = defaultdict(int)

        # ディクショナリの初期化
        # Featureクラスのインスタンスを格納
        # ある素性を含むカテゴリに属するデータ数
        self.features = {}

        # 学習されたデータの数
        self.training_count = 0

        # ゼロ頻度問題を解決するためスムージングの値
        # alphaの値が1の場合はラプラススムージング
        self.alpha = 1


    ## 学習フェーズ
    def learn(self, category, features):
        self.categories[category] += 1
        self.training_count += 1

        for f in features:

            # NaiveBayesClassifierクラスのfeaturesのkeyの存在判定
            # keyが存在しなければ新しくFeatureインスタンスを作成する
            if f not in self.features:
                self.features[f] = Feature(f)

            # Featureの__setitem__が呼ばれる
            self.features[f][category] += 1


    ## 適用フェーズ
    def classifly(self, features):
        result = None
        max_score = 0

        ## cはcategoriesのkey、つまりカテゴリ名
        for c in self.categories:

            # カテゴリcの出現回数 + α / データの総数 + カテゴリ数 * α (= Pc)
            score = float(self.categories[c] + self.alpha) / (self.training_count + len(self.categories) * self.alpha)

            for f in self.features:
                # 素性fを含むカテゴリcの出現回数 + α / カテゴリcに属するデータの総数 + 2α (= Pf,c)
                score *= float(self.features[f][c] + self.alpha) / (self.categories[c] + 2 * self.alpha)

            # scoreが一番高いカテゴリを返す
            if max_score < score:
              result, max_score = c, score

        return result


    def get_alpha(self):
        self.alpha

    def set_alpha(self, value):
        self.alpha = value


def main():
    # 学習用データ
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

    # 適用フェーズ
    print (classifier.classifly(test_data))

if __name__ == "__main__":
    main()
