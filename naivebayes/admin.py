from django.contrib import admin
from naivebayes.models import Element, Category, Feature, FeatureCategory

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Element)
admin.site.register(Category)
admin.site.register(Feature)
admin.site.register(FeatureCategory)
