from django.conf.urls import url, include
from django.contrib import admin
from Site import urls as SiteUrls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('Consultar.urls')),
    url(r'^', include(SiteUrls, namespace="home")),
]
