import uuid
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blogger(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    about = models.TextField(max_length=2000, null=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # slug = models.SlugField(default=str(f'{first_name}-{last_name}'), null=False)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    
class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    # a blogger can be an author of many posts but each post
    # would have only one author: Many-to-one relationship
    author = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    publish_date = models.DateField()
    content = models.TextField()

    def __str__(self) -> str:
        return self.title
    

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="UUID for the comment from the user")
    on_blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)

    def __str__(self) -> str:
        return f'{self.user}: {self.id}'