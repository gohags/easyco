from django.conf import settings
from django.http.response import HttpResponse

class CustomAuthMiddleware:
    def __init__(self, get_response,*args, **kwargs):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request, *args, **kwargs):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        path = request.path_info.lstrip('/')
        if 'prometheus' in path:
            key = getattr(settings,'PROMETHEUS_KEY',None)
            print(key)
            auth = request.GET.get('key')
            print(auth)
            print(request.GET)
            if key is not None and key == auth:
                request.GET = {}
                return self.get_response(request)
            else:
                return HttpResponse('Unauthorized')
        # todo: do something you want in response 
        return self.get_response(request)