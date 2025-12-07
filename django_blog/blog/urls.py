from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # Blog posts
    path('posts/', views.post_list, name='post_list'),
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),

    # User authentication
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    # User profile
    path('profile/', views.profile_view, name='profile'),
]
