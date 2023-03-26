from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models


# Create your views here.
def home(request):
    return render(request, 'home.html')


class BloggerList(LoginRequiredMixin, generic.ListView):
    model = models.Blogger


class BloggerDetail(LoginRequiredMixin, generic.DetailView):
    model = models.Blogger


class BlogPostList(LoginRequiredMixin, generic.ListView):
    model = models.BlogPost


class BlogPostDetail(LoginRequiredMixin, generic.DetailView):
    model = models.BlogPost


# class BloggerLogin(LoginView):
#     redirect_authenticated_user = True

#     def get_success_url(self) -> str:
#         return reverse_lazy('tasks')
    
#     def form_invalid(self, form: _FormT) -> HttpResponse:
#         return 