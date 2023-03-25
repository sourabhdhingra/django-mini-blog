from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Blogger)
admin.site.register(models.BlogPost)
