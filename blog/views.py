from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
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

class CreateUpdateView(UpdateView):

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except AttributeError:
            return None

class BloggerCreate(LoginRequiredMixin, CreateView):
    form_class = forms.BloggerForm
    template_name = 'blog/blogger_form.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['user_linked_blogger'] = models.Blogger.objects.filter(user=self.request.user)

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        blogger = form.save(commit=False)
        blogger.user = self.request.user
        blogger.save()
        self.object = blogger
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self) -> str:
        return reverse_lazy('blogger-detail', kwargs={'pk': self.object.pk})
