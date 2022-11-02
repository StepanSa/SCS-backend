from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('api.urls')),
]

urlpatterns += staticfiles_urlpatterns()
