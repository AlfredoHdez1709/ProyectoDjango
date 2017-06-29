from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from Consultar import views

urlpatterns = [
    url(r'^restaurantes/$', views.RestauranteList.as_view()),
    url(r'^esteticas/$', views.EsteticaList.as_view()),
    url(r'^hoteles/$', views.HotelesList.as_view()),
    url(r'^veterinarias/$', views.VeterinariasList.as_view()),
    

]

urlpatterns = format_suffix_patterns(urlpatterns)