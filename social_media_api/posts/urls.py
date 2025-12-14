from django.urls import path
from .views import feed
from django.urls import path
from .views import feed, like_post, unlike_post

urlpatterns = [
    path('feed/', feed),
]

urlpatterns = [
    path('feed/', feed),
    path('posts/<int:pk>/like/', like_post),
    path('posts/<int:pk>/unlike/', unlike_post),
]
