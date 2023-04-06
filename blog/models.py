import uuid
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import IntegrityError
import logging



# Create your models here.
class Blogger(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    about = models.TextField(max_length=2000, null=True)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'
    
    def get_absolute_url(self) -> str:
        return reverse_lazy('blogger-detail', kwargs={'pk': self.pk})
    
    
class BlogPost(models.Model):
    title = models.CharField(max_length=300, unique_for_date='publish_date')
    # a blogger can be an author of many posts but each post
    # would have only one author: Many-to-one relationship
    author = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(editable=False, auto_now_add=True)
    last_updated = models.DateTimeField(editable=False, auto_now=True)
    content = models.TextField()

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self) -> str:
        return reverse_lazy('blogpost-detail', kwargs={'pk': self.pk})
    

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="UUID for the comment from the user")
    on_blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)

    def __str__(self) -> str:
        return f'{self.user}: {self.id}'
    

# permissions
# class BlogPostAuthorPermission(Permission):
#     class Meta:
#         proxy = True
#         verbose_name = 'Can edit own blog post'

#     def has_permission(self, user, obj=None):
#         if obj is None:
#             return False
#         return obj.author == user

# # creating the permission to edit own blog post
# try:
#     content_type = ContentType.objects.get_for_model(BlogPost)
#     permission = BlogPostAuthorPermission.objects.create(
#         codename='edit_own_blog_post',
#         name='Can edit own blog post',
#         content_type= content_type,
#     )
# except IntegrityError as e:
#     if 'UNIQUE constraint failed' in e.args[0]:
#         logging.warn('Permisssion with codename already exist')