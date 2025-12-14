from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, feed, like_post, unlike_post

# /posts/int:pk/like/
# /posts/int:pk/unlike/

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('posts/<int:pk>/like/', like_post),
    path('posts/<int:pk>/unlike/', unlike_post),
    path('feed/', feed),
    path('', include(router.urls)),
]
