from django.conf import settings
from django.contrib import auth


class DebugAutologinMiddleware(object):


  def process_request(self, request):

    if settings.DEBUG:
      if request.user.is_authenticated():
        return
      user = auth.authenticate(username='admin', password='password')
      if user:
        request.user = user
        auth.login(request, user)

