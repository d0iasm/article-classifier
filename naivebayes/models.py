from django.db import models

class Element(models.Model):
    categories = models.IntegerField()
    training_count = models.IntegerField()
    alpha = models.IntegerField(default=1)

class Feature(models.Model):
    features = models.CharField(max_length=200)

class Count(models.Model):
    feature = models.OneToOneField(
        Feature,
        on_delete = models.CASCADE,
        primary_key = True,
    )
    data_count = models.IntegerField()
