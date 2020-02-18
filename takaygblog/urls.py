from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.urls import path, include

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),

    path('markdownx/', include('markdownx.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)