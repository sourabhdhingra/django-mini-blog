from . import models

def get_userlinked_blogger(request):
    blogger = None
    if request.user.is_authenticated:
        queryset = models.Blogger.objects.filter(user=request.user)
        blogger = queryset[0] if queryset else None
    return {
        'userlinked_blogger': blogger
    }