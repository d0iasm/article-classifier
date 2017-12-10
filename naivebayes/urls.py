from django.conf.urls import url

from . import views


app_name = "naivebayes"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^learn/$', views.learn, name='learn'),
]
