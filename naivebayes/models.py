from django.db import models

class Element(models.Model):
    training_count = models.IntegerField()
    alpha = models.IntegerField(default=1)

class Category(models.Model):
    categories = models.CharField(max_length=100)

class CategoryCount(models.Model):
    category = models.OneToOneField(
        Category,
        on_delete = models.CASCADE,
        primary_key = True,
    )
    data_count = models.IntegerField()

class Feature(models.Model):
    features = models.CharField(max_length=200)

class FeatureCount(models.Model):
    feature = models.OneToOneField(
        Feature,
        on_delete = models.CASCADE,
        primary_key = True,
    )
    data_count = models.IntegerField()
