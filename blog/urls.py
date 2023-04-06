from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.RegisterFormView.as_view(), name='register'),
    path('bloggers/', views.BloggerList.as_view(), name='bloggers'),
    path('blogger/<int:pk>', views.BloggerDetail.as_view(), name='blogger-detail'),
    path('blogger/create', views.BloggerCreate.as_view(), name='blogger-create'),
    path('blogger/<int:pk>/update', views.BloggerUpdate.as_view(), name='blogger-update'),
    path('blogs/', views.BlogPostList.as_view(), name='blogs'),
    path('blogs/<str:username>', views.BlogPostList.as_view(), name='user-blogs'),
    path('blog/<int:pk>', views.BlogPostDetail.as_view(), name='blogpost-detail'),
    path('blog/create', views.BlogPostCreate.as_view(), name='blogpost-create'),
    path('blog/<int:pk>/update', views.BlogPostUpdate.as_view(), name='blogpost-update'),
    path('blog/<int:pk>/delete', views.BlogPostDelete.as_view(), name='blogpost-delete'),
]