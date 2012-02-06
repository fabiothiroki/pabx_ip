from django.contrib.auth.models import User
from pabx_ip.accounts.models import UserProfile

from django.core.exceptions import PermissionDenied

def is_admin(function):

    def _inner(request, *args, **kwargs):

        if request.user.username == 'root':
            return function(request, *args, **kwargs)
        else:
            up = UserProfile.objects.get(profile=request.user.id)

            if not up.admin:
                raise PermissionDenied           
            return function(request, *args, **kwargs)
        
    return _inner