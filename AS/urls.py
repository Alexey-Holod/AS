from django.contrib import admin
from django.conf.urls.static import static
from django.template.defaulttags import url
from django.urls import path, include
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('', include('home.urls'), name='home'),
    path('users/', include('users.urls'), name='users'),
    path('auth_user_do/', include('auth_user_do.urls')),
    path('delivery/', include('delivery.urls'), name='delivery'),
    path('moder/', include('modersite.urls')),
    path('kasandra/', admin.site.urls),
]

#url('social-auth/', include('social.apps.django_app.urls', namespace='social')),

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)