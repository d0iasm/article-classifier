from django.db import models


class Element(models.Model):
    training_count = models.IntegerField()
    alpha = models.IntegerField(default=1)


class Category(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class FeatureCategory(models.Model):
    feature = models.ForeignKey(
        Feature,
        on_delete = models.CASCADE
    )
    name = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
