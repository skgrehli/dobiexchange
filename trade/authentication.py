from rest_framework import authentication
from rest_framework import exceptions
from app.models import Key


class AccessKeyAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        
        access_key = request.GET.get("access_key", None)
        if not access_key:
            raise exceptions.NotFound("Access key not provided.")
        try:
            user = Key.objects.get(access_key=access_key)
        except Key.DoesNotExist:
            raise exceptions.PermissionDenied("No User found with the access key")
        except ValueError:
            raise exceptions.ValidationError("Badly formed hexadecimal UUID string")

        return (user, None)