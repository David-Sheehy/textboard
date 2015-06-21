from django.conf.urls import url
from hash_board import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^thread/(?P<thread_id>[0-9]*($|/))', views.thread),
    url(r'^tag/(?P<tag_id>[0-9]*($|/))', views.tag,),
]
