from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


api_urlpatterns = [
    path('rooms/', include('apps.rooms.api.urls')),
    path('comments/', include('apps.comments.api.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.rooms.urls')),
    path('', include('apps.users.urls')),
    path('', include('apps.restaurants.urls')),
    path('', include('apps.pages.urls')),
    path('', include('apps.comments.urls')),


]
urlpatterns += api_urlpatterns

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
