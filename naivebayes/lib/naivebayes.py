import math
import sys
from collections import defaultdict

from naivebayes.models import Element, Category, Feature, FeatureCategory


class NaiveBayesClassifier:
    """ NaiveBayes """

    def __init__(self):
        element = Element.objects.get(id=1)

        self.categories = Category.objects.values_list('name', 'count')

        self.features = Feature.objects.values_list('name', flat=True)

        self.training_count = element.training_count

        # ゼロ頻度問題を解決するためスムージングの値
        # alphaの値が1の場合はラプラススムージング
        self.alpha = element.alpha


    def learn(self, category, features):
        self.training_count += 1

        current_category = Category.objects.get_or_create(name=category)
        category_count = current_category[0].count
        category_count += 1
        Category.objects.filter(name=category).update(
            count = category_count
        )

        for f in features:

            current_feature = Feature.objects.get_or_create(name=f)

            if current_feature[0].featurecategory_set.filter(name=category).exists() == False:

                new_feature_category = FeatureCategory(
                    feature = current_feature[0],
                    name = category,
                    count = 0
                )
                new_feature_category.save()

            feature_category_count = current_feature[0].featurecategory_set.get(name=category).count
            feature_category_count += 1
            FeatureCategory.objects.filter(name=f).update(
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

            # カテゴリcの出現回数 + α / データの総数 + カテゴリ数 * α (= Pc)
            score = float(Category.objects.get(name=c[0]).count + self.alpha) / (self.training_count + Category.objects.count() * self.alpha)

            for f in self.features:
                if Feature.objects.filter(name=f).exists() == True:
                    if Feature.objects.get(name=f).featurecategory_set.filter(name=c[0]).exists() == True:
                        feature_f_c_count = Feature.objects.get(name=f).featurecategory_set.filter(name=c[0])[0].count
                else:
                    feature_f_c_count = 0

                # 素性fを含むカテゴリcの出現回数 + α / カテゴリcに属するデータの総数 + 2α (= Pf,c)
                score *= float(feature_f_c_count + self.alpha) / (c[1] + 2 * self.alpha)

            if max_score < score:
              result, max_score = c[0], score

        return result


    def reset(self):
        Element.objects.filter(id=1).update(
            training_count = 0,
            alpha = 1
        )
        Category.objects.all().delete()
        Feature.objects.all().delete()
        FeatureCategory.objects.all().delete()


    def get_alpha(self):
        self.alpha


    def set_alpha(self, value):
        self.alpha = value


    def get_training_count(self):
        return self.training_count
