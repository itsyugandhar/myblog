
from django.contrib import admin
from django.urls import path
from django.urls import include

from home import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('about/',views.about,name = 'about'),
    path("profile/<str:username>/", views.user_profile, name="user_profile"),
    path('contact/',views.contact,name = 'contact'),
    path('search',views.search,name = 'search'),
    path('signup',views.blogsignup,name = 'blogsignup'),
    path('login',views.bloglogin,name = 'bloglogin'),
    path('logout',views.bloglogout,name = 'bloglogout'),
     path('profile/', views.profile, name='profile'),


]
