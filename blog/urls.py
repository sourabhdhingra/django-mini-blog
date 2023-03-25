from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bloggers', views.BloggerList.as_view(), name='bloggers'),
    path('blogger/<int:pk>', views.BloggerDetail.as_view(), name='blogger-detail'),
    path('blogs', views.BlogPostList.as_view(), name='blogs'),
    path('blog/<int:pk>', views.BlogPostDetail.as_view(), name='blogpost-detail'),
]