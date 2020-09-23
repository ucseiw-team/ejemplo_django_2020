"""noticias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from sitio.views import (
    inicio, ejemplo_form, ejemplo_form_copado, ejemplo_ajax, publicidad_ajax,
    cantidad_noticias_ajax, subir_foto, ejemplo_refresco_automatico
)

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('inicio/', inicio),
    path('ejemplo_form/', ejemplo_form),
    path('ejemplo_form_copado/', ejemplo_form_copado),
    path('ejemplo_refresco_automatico/', ejemplo_refresco_automatico),
    path('ejemplo_ajax/', ejemplo_ajax),
    path('ajax/publicidad/', publicidad_ajax),
    path('ajax/cantidad_noticias/', cantidad_noticias_ajax),
    path('subir_foto/', subir_foto),
    path('admin/', admin.site.urls),
    path('search/', include('haystack.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
