from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.RegisterFormView.as_view(), name='register'),
    path('bloggers/', views.BloggerList.as_view(), name='bloggers'),
    path('blogger/create', views.BloggerCreate.as_view(), name='blogger-create'),
    path('blogger/<slug:slug>', views.BloggerDetail.as_view(), name='blogger-detail'),
    path('blogger/<slug:slug>/update', views.BloggerUpdate.as_view(), name='blogger-update'),
    path('blogger/<slug:slug>/delete', views.BloggerDelete.as_view(), name='blogger-delete'),
    path('blogposts/', views.BlogPostList.as_view(), name='blogs'),
    path('blogposts/<str:username>', views.BlogPostList.as_view(), name='user-blogs'),
    path('blogpost/create', views.BlogPostCreate.as_view(), name='blogpost-create'),
    path('blogpost/<slug:slug>', views.BlogPostDetail.as_view(), name='blogpost-detail'),
    path('blogpost/<slug:slug>/update', views.BlogPostUpdate.as_view(), name='blogpost-update'),
    path('blogpost/<slug:slug>/delete', views.BlogPostDelete.as_view(), name='blogpost-delete'),
    path('blogpost/<slug:slug>/comment/create', views.CommentCreate.as_view(), name='comment-create'),
    path('comment/<slug:slug>/update', views.CommentUpdate.as_view(), name='comment-update'),
    path('comment/<slug:slug>/delete', views.CommentDelete.as_view(), name='comment-delete'),
]