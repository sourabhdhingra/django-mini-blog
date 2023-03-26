from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView

from . import models
# from django.template import loader

# Create your views here.
def home(request):
    return render(request, 'home.html')


class BloggerList(generic.ListView):
    model = models.Blogger


class BloggerDetail(generic.DetailView):
    model = models.Blogger


class BlogPostList(generic.ListView):
    model = models.BlogPost


class BlogPostDetail(generic.DetailView):
    model = models.BlogPost


# class BloggerLogin(LoginView):
#     redirect_authenticated_user = True

#     def get_success_url(self) -> str:
#         return reverse_lazy('tasks')
    
#     def form_invalid(self, form: _FormT) -> HttpResponse:
#         return 