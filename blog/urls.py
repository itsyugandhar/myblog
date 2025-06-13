from django.contrib import admin
from django.urls import path
from django.urls import include
from blog import views

urlpatterns = [
    path('postComment', views.postComment, name='postComment'),
    path('create/', views.create_blog, name='create_blog'),
    path('',views.blogpage,name = 'blogpage'),
    path('<str:slug>',views.blogpost,name = 'blogpost'),

]

# urlpatterns = [
#     path('postComment', views.postComment, name='postComment'),
#     path('create/', views.create_blog, name='create_blog'),  # ← Add this line
#     path('', views.blogpage, name='blogpage'),
#     path('<str:slug>', views.blogpost, name='blogpost'),
# ]