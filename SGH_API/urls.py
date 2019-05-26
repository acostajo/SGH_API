"""SGH_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ficha.urls')),
    path('', include('panolab.urls')),
    path('', include('consulta.urls')),
    path('', include('orinasimple.urls')),
    path('', include('orinasimpledatoslab.urls')),
    path('', include('enfermedad.urls')),
    path('', include('comorbilidades.urls')),
    path('', include('efectoadverso.urls')),
    path('', include('efectoadverso_consulta.urls')),
    path('', include('eventocardio_ficha.urls')),
    path('', include('eventocardiovascular.urls')),
    path('', include('fames.urls')),
    path('', include('famesficha.urls')),
    path('', include('maniextraarti.urls')),
    path('', include('manifestacion.urls')),
    path('', include('ordenestudio.urls')),
    path('', include('estudio.urls')),
    path('', include('famesficha.urls')),
    url(r'^archivo/', include('archivoestudio.urls')),
    path('', include('archivo.urls')), 
    path('', include('agenda.urls')), 
    path('', include('turno.urls')), 
    path('', include('turno_distribucion.urls')), 
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)