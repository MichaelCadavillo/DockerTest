# data/urls.py
from django.conf.urls import url
from data import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]