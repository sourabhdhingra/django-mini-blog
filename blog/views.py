from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.utils.text import slugify
import logging
from . import models, forms
from . import utils


# Create your views here.
def home(request):
    return render(request, 'home.html')

class RegisterFormView(CreateView):
    template_name = 'register.html'
    form_class = forms.RegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form) -> HttpResponse:
        return super().form_valid(form)

class BloggerList(LoginRequiredMixin, generic.ListView):
    model = models.Blogger


class BloggerDetail(LoginRequiredMixin, generic.DetailView):
    model = models.Blogger


class BloggerCreate(LoginRequiredMixin, CreateView):
    form_class = forms.BloggerForm
    template_name = 'blog/blogger_form.html'

    
    # we need to populate Blogger instance's user with current logged in user
    # before committing to the model
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        blogger = form.save(commit=False) # so that blogger user can be updated
        blogger.user = self.request.user # setting the authenticated user to blogger user
        blogger.slug = slugify(self.request.user.username)
        blogger.save() # committing the blogger
        self.object = blogger
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self) -> str:
        return reverse_lazy('blogger-detail', kwargs={'slug': self.object.slug})


class BloggerUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Blogger
    form_class = forms.BloggerForm
    template_name = 'blog/blogger_form.html'

    def test_func(self):
        return self.request.user == self.get_object().user

class BloggerDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Blogger
    success_url = '/'

    def test_func(self):
        return self.request.user == self.get_object().user

class BlogPostList(LoginRequiredMixin, generic.ListView):
    model = models.BlogPost

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'username' in self.kwargs:
            blogger_name = self.kwargs['username']
            if blogger_name:
                found_user = models.User.objects.get(username=blogger_name)
                found_blogger = models.Blogger.objects.get(user=found_user)
                queryset =  models.BlogPost.objects.filter(author=found_blogger)
        return queryset


class BlogPostDetail(LoginRequiredMixin, generic.DetailView):
    model = models.BlogPost


class BlogPostCreate(LoginRequiredMixin, CreateView):
    model = models.BlogPost
    fields = ['title', 'content']


    def form_valid(self, form) -> HttpResponse:
        # saving the blogpost but first mapping the logged in user to the blogger
        blogpost = form.save(commit=False)
        blogpost.author = models.Blogger.objects.get(user=self.request.user)
        blogpost.slug = slugify(blogpost.title)
        blogpost.save()
        self.object = blogpost
        return HttpResponseRedirect(self.get_success_url())


    def get_success_url(self) -> str:
        return reverse_lazy('blogpost-detail', kwargs={'slug': self.object.slug})

class BlogPostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.BlogPost
    fields = ['title', 'content']

    def test_func(self):
        logging.warn(f"self.request.user = {self.request.user} and blogpost author = {self.get_object().author.user}")
        return self.request.user == self.get_object().author.user


class BlogPostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.BlogPost

    def get_success_url(self) -> str:
        return reverse_lazy('user-blogs', kwargs={'username': self.get_object().author.user.username})
    
    def test_func(self):
        return self.request.user == self.get_object().author.user


class CommentCreate(LoginRequiredMixin, CreateView):
    model = models.Comment
    fields = ['content']

    def get_success_url(self) -> str:
        return reverse_lazy('blogpost-detail', kwargs={'slug': self.kwargs['slug']})
    
    def form_valid(self, form) -> HttpResponse:
        # assigning logged in user to the commentor
        form.instance.commentor = self.request.user

        # associate comment with the blog post id
        # we use pk coming from the URL itself to fetch the blogpost
        form.instance.on_blogpost  = get_object_or_404(models.BlogPost, slug = self.kwargs['slug'])

        # populate slug based upon the fields - content's first 50 chars clubbed with posted_on
        form.instance.slug = slugify(f"{form.instance.commentor.username}-{slugify(form.instance.content[:50])}-{utils.get_random_alphanumeric()}")
        return super(CommentCreate, self).form_valid(form)


class CommentUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Comment
    fields = ['content']

    def get_success_url(self) -> str:
        # we use self.get_object() as the URL used for update comment has PK for comment model
        # and not the blogpost itself
        return reverse_lazy('blogpost-detail', kwargs={'slug': self.get_object().on_blogpost.slug})
    
    def test_func(self):
        return self.get_object().commentor == self.request.user


class CommentDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Comment

    def get_success_url(self) -> str:
        # we use self.get_object() as the URL used for update comment has PK for comment model
        # and not the blogpost itself
        return reverse_lazy('blogpost-detail', kwargs={'slug': self.get_object().on_blogpost.slug})
    
    def test_func(self):
        return self.get_object().commentor == self.request.user

