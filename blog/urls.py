from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bloggers', views.BloggerList.as_view(), name='bloggers'),
]