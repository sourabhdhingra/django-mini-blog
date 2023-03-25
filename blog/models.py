from django.db import models

# Create your models here.
class Blogger(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    about = models.TextField(max_length=2000, null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    
