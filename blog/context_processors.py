from . import models

def get_userlinked_blogger(request):
    blogger = models.Blogger.objects.filter(user=request.user) if request.user.is_authenticated else None
    return {
        'userlinked_blogger': blogger
    }