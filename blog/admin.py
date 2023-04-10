from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from . import models, utils
from django.utils.text import slugify


class BloggerInline(admin.StackedInline):
    model = models.Blogger
    can_delete = False
    verbose_name_plural = 'blogger'


class BloggerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['about']}

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.user.username)
        return super().save_model(request, obj, form, change)


class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}

class CommentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['content']}

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(f"{obj.commentor.username}-{slugify(obj.content[:50])}-{utils.get_random_alphanumeric()}") 
        return super().save_model(request, obj, form, change)


# Register your models here.
admin.site.register(models.Blogger, BloggerAdmin)
admin.site.register(models.BlogPost, BlogPostAdmin)
admin.site.register(models.Comment, CommentAdmin)


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (BloggerInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
