from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from usuarios.views import UsuarioViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('usuarios.urls')),
    path('api/', include('api.urls')),
    path('', include('doacoes.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)