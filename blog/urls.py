from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bloggers', views.BloggerList.as_view(), name='bloggers'),
    path('blogger/<int:pk>', views.BloggerDetail.as_view(), name='blogger-detail'),
    path('blogger/create', views.BloggerCreate.as_view(), name='blogger-create'),
    path('blogs', views.BlogPostList.as_view(), name='blogs'),
    path('blog/<int:pk>', views.BlogPostDetail.as_view(), name='blogpost-detail'),
    path('register', views.RegisterFormView.as_view(), name='register'),
    path('blog/create', views.BlogPostCreate.as_view(), name='blogpost-create'),
]