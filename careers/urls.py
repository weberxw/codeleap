from django.conf.urls import url
from careers import views

urlpatterns = [
    url(r'posts/(?P<pk>[0-9]+)/', views.Posts.as_view()),
    url(r'posts/', views.Posts.as_view()),
]
