from django.shortcuts import render
from django.views import generic

from . import models
# from django.template import loader

# Create your views here.
def home(request):
    return render(request, 'home.html')


class BloggerList(generic.ListView):
    model = models.Blogger


class BloggerDetail(generic.DetailView):
    model = models.Blogger