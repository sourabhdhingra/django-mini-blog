from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from blog import models

# Register your models here.
admin.site.register(models.Blogger)
admin.site.register(models.BlogPost)
admin.site.register(models.Comment)

class BloggerInline(admin.StackedInline):
    model = models.Blogger
    can_delete = False
    verbose_name_plural = 'blogger'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (BloggerInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
