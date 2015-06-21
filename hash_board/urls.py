from django.conf.urls import url
from hash_board import views

urlpatterns = [
    url(r'^$', views.index),
]
