from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from . import models, forms


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


class RegisterFormView(CreateView):
    template_name = 'register.html'
    form_class = forms.RegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form) -> HttpResponse:
        return super().form_valid(form)


class BlogPostCreate(LoginRequiredMixin, CreateView):
    model = models.BlogPost
    success_url = reverse_lazy('blogpost-detail')
    fields = '__all__'

