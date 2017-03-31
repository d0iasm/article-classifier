import math
import sys
from collections import defaultdict

from naivebayes.models import Element, Category, Feature, FeatureCategory


class NaiveBayesClassifier:
    """ NaiveBayes """

    def __init__(self):
        element = Element.objects.get(id=1)

        # 各カテゴリのデータの数
        # self.categories = defaultdict(int)
        # self.categories = Category.objects.values_list('name', flat=True)
        self.categories = Category.objects.values_list('name', 'count')

        # ディクショナリの初期化
        # Featureクラスのインスタンスを格納
        # ある素性を含むカテゴリに属するデータ数
        # self.features = {}
        self.features = Feature.objects.values_list('name', flat=True)

        # 学習されたデータの数
        # self.training_count = 0
        self.training_count = element.training_count

        # ゼロ頻度問題を解決するためスムージングの値
        # alphaの値が1の場合はラプラススムージング
        # self.alpha = 1
        self.alpha = element.alpha


    def learn(self, category, features):
        self.training_count += 1
        # self.categories[category] += 1

        current_category = Category.objects.get_or_create(name=category)
        # if category in self.categories:
        # if current_category[1] == True:
        #     new_category_count = CategoryCount(
        #         category = current_category[0],
        #         data_count = 0
        #     )
        #     new_category_count.save()

        # category_count = current_category[0].categorycount.data_count
        category_count = current_category[0].count
        category_count += 1
        Category.objects.filter(name=current_category[0].name).update(
            count = category_count
        )
        # CategoryCount.objects.filter(category=current_category[0]).update(
        #     data_count = category_count
        # )

        for f in features:

            current_feature = Feature.objects.get_or_create(name=f)

            # NaiveBayesClassifierクラスのfeaturesのkeyの存在判定
            # keyが存在しなければ新しくFeatureインスタンスを作成する
            # if f not in self.features:
                # new_feature = Feature(name=f)
                # new_feature.save()
                # new_feature_count = FeatureCount(
                #     feature = new_feature,
                #     data_count = 0
                # )
                # new_feature_count.save()

                # self.features[f] = Feature(f)

            if current_feature[0].featurecategory_set.filter(name=category).exists() == False:
            # if current_feature[1] == True:
                # new_feature_count = FeatureCount(
                #     feature = current_feature[0],
                #     data_count = 0
                # )
                # new_feature_count.save()
                new_feature_category = FeatureCategory(
                    feature = current_feature[0],
                    name = category,
                    count = 0
                )
                new_feature_category.save()


            # Featureの__setitem__が呼ばれる
            # self.features[f][category] += 1

            # current_feature = Feature.objects.get(name=f)
            # feature_current_count = current_feature[0].featurecount.data_count
            # feature_current_count += 1
            # FeatureCount.objects.filter(feature=current_feature[0]).update(
            #     data_count = feature_current_count
            # )

            # current_feature[0].featurecategory_set.add(new_feature_category)
            feature_category_count = current_feature[0].featurecategory_set.get(name=category).count
            feature_category_count += 1
            FeatureCategory.objects.filter(name=current_feature[0].name).update(
                count = feature_category_count
            )

        Element.objects.filter(id=1).update(
            training_count = self.training_count,
            alpha = self.alpha
        )


    def classifly(self, features):
        result = None
        max_score = 0

        for c in self.categories:
            print(c[0])
            break

            # カテゴリcの出現回数 + α / データの総数 + カテゴリ数 * α (= Pc)
            # score = float(self.categories[c] + self.alpha) / (self.training_count + len(self.categories) * self.alpha)
            score = float(Category.objects.get(name=c[0]).count + self.alpha) / (self.training_count + Category.objects.count() * self.alpha)

            for f in self.features:
                # 素性fを含むカテゴリcの出現回数 + α / カテゴリcに属するデータの総数 + 2α (= Pf,c)
                # score *= float(self.features[f][c] + self.alpha) / (self.categories[c] + 2 * self.alpha)
                score *= float(Feature.objects.get(name=f).featurecategory_set.get(name=c[0]).count + self.alpha) / (c[1] + 2 * self.alpha)

            # scoreが一番高いカテゴリを返す
            if max_score < score:
              result, max_score = c[0], score

        return result

    def reset(self):
        pass

    def get_alpha(self):
        self.alpha

    def set_alpha(self, value):
        self.alpha = value

    def get_training_count(self):
        return self.training_count
