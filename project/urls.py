from django.conf.urls import include, url
from django.contrib import admin
import auto_create_superuser as superuser

superuser.create()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app_landing.views.index'),
]
