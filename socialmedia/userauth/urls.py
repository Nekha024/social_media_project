from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from userauth import views

urlpatterns = [
    path('',views.home),
    path('signup/',views.signup,name='signup'),
    path('loginn/',views.loginn),
    path('logoutt/',views.logoutt),
    path('upload',views.upload),
    path('like-post/<str:id>', views.likes, name='like-post'),
    path('#<str:id>', views.home_post),
    path('explore',views.explore),
    path('profile/<str:id_user>', views.profile),
    path('delete/<str:id>', views.delete),
    path('search-results/', views.search_results, name='search_results'),
    path('follow', views.follow, name='follow'),
    
]