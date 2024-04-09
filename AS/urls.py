from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('', include('home.urls')),
    path('kasandra/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('moder/', include('modersite.urls')),
]
