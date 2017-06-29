from django.shortcuts import render
from Categorias.models import Restaurantes, Esteticas, Hoteles, Veterinarias
from Consultar.serializers import RestaurantesSerializer, EsteticasSerializer, HotelesSerializer, VeterinariasSerializer
from rest_framework import generics


class RestauranteList(generics.ListCreateAPIView):
    queryset = Restaurantes.objects.all()
    serializer_class = RestaurantesSerializer


class EsteticaList(generics.ListCreateAPIView):
    queryset = Esteticas.objects.all()
    serializer_class = EsteticasSerializer

class HotelesList(generics.ListCreateAPIView):
    queryset = Hoteles.objects.all()
    serializer_class = HotelesSerializer

class VeterinariasList(generics.ListCreateAPIView):
    queryset = Veterinarias.objects.all()
    serializer_class = VeterinariasSerializer

