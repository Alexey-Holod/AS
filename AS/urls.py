from django.contrib import admin
from django.conf.urls.static import static
from django.template.defaulttags import url
from django.urls import path, include
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('', include('home.urls')),
    path('kasandra/', admin.site.urls),
    path('moder/', include('modersite.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)