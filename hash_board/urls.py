from django.conf.urls import url
from hash_board import views

urlpatterns = [

    url(r'^$', views.index, name="hb_index"),
    url(r'^thread/(?P<thread_number>[0-9]*($|/))', views.thread, name="thread_page"),
    url(r'^tag/(?P<tag_name>.*($|/))', views.tag, name="tag_page"),

]
