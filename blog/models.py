import uuid
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy


# Create your models here.
class Blogger(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    about = models.TextField(max_length=2000, null=True)
    slug = models.SlugField(max_length=50)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'
    
    def get_absolute_url(self) -> str:
        return reverse_lazy('blogger-detail', kwargs={'slug': self.slug})
    
    
class BlogPost(models.Model):
    title = models.CharField(max_length=300, unique_for_date='publish_date')
    # a blogger can be an author of many posts but each post
    # would have only one author: Many-to-one relationship
    author = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(editable=False, auto_now_add=True)
    last_updated = models.DateTimeField(editable=False, auto_now=True)
    content = models.TextField()
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ['-publish_date']


    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self) -> str:
        return reverse_lazy('blogpost-detail', kwargs={'slug': self.slug})
    

class Comment(models.Model):
    on_blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    commentor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    content = models.TextField(max_length=300)
    posted_on = models.DateTimeField(editable=False, auto_now=True)
    edited_at = models.DateTimeField(editable=False, auto_now_add=True)
    slug = models.SlugField(max_length=100)

    class Meta:
        ordering = ['posted_on']

    def __str__(self) -> str:
        return f'{self.commentor.username} :{self.content[:30]}'