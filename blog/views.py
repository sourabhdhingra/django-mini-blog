from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
import logging
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
    fields = '__all__'

    def get_success_url(self) -> str:
        return reverse_lazy('blogpost-detail', kwargs={'pk': self.object.pk})


class BloggerCreate(LoginRequiredMixin, CreateView):
    form_class = forms.BloggerForm
    template_name = 'blog/blogger_form.html'

    
    # we need to populate Blogger instance's user with current logged in user
    # before committing to the model
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        blogger = form.save(commit=False) # so that blogger user can be updated
        blogger.user = self.request.user # setting the authenticated user to blogger user
        blogger.save() # committing the blogger
        self.object = blogger
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self) -> str:
        return reverse_lazy('blogger-detail', kwargs={'pk': self.object.pk})

class BloggerUpdate(LoginRequiredMixin, UpdateView):
    model = models.Blogger
    form_class = forms.BloggerForm
    template_name = 'blog/blogger_form.html'
    template_name_suffix = '_update_form'
    