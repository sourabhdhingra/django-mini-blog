import uuid
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blogger(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    about = models.TextField(max_length=2000, null=True)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'
    
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